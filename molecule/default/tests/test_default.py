import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_consul_group(host):
    assert host.group('consul').exists


def test_consul_user(host):
    user = host.user('consul')

    assert user.exists
    assert user.group == 'consul'


@pytest.mark.parametrize('folder', [
  '/usr/bin',
  '/etc/consul',
  '/etc/consul/consul.d',
  '/var/consul',
  '/var/run/consul'
])
def test_consul_folders(host, folder):
    file = host.file(folder)

    assert file.exists
    assert file.is_directory
    assert file.user == 'consul'
    assert file.group == 'consul'


def test_consul_dependencies(host):
    pkg = host.package('unzip')

    assert pkg.is_installed


def test_consul_binary_is_installed(host):
    file = host.file('/usr/bin/consul')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755


@pytest.mark.parametrize('file', [
  '/etc/consul/config.json',
  '/etc/systemd/system/consul.service',
])
def test_consul_configurations(host, file):
    file = host.file(file)

    assert file.exists
    assert file.mode == 0o600


def test_consul_systemd_enabled(host):
    assert host.service('consul.service').is_enabled
    assert host.service('consul.service').is_running


def test_consul_backup_binary_is_installed(host):
    file = host.file("/usr/bin/consul-backinator")

    assert file.exists
    assert file.mode == 0o777


def test_consul_backup_was_scheduled(host):
    assert "consul-backinator backup" in host.check_output("crontab -l")
