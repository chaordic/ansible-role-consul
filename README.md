# Ansible Role: Consul
An ansible role to install and configure Consul agent, this role was customized to use Consul in AWS.

## Requirements
- [Ansible >= 2.5](https://ansible.com/)
- OS based on systemd


## Role Variables

Please look at the [defaults/main.yml](defaults/main.yml) to see all default variables.

```yml
---
consul_config:
  server: true
  data_dir: "/var/consul"
  ui: true
```
The mandatory variable is the `consul_config`, this dict is composed by [Consul options](https://www.consul.io/docs/agent/options.html).

```yml
---
consul_backup_config:
  file: "/tmp/consul.bkp"
```
The mandatory variable is the `consul_backup_config`, this dict is composed by [Consul Backinator options](https://github.com/myENA/consul-backinator#backup-options).

## Example Playbook

```yml
---
- name: "Consul server"
  hosts: servers
  gather_facts: true
  vars:
    # Consul
    consul_config:
      server: true
      datacenter: chaordic
      data_dir: "{{ consul_data_dir }}"
      bind_addr: "{{ ansible_default_ipv4.address }}"
      ui: true
      client_addr: "0.0.0.0"

    # Consul Backup
    consul_backup_enabled: true
    consul_backup_hour: 12
    consul_backup_config:
      file: "/tmp/consul.bkp"

  roles:
    - role: ansible-role-consul
      tags: consul
```


## Development

### Requirements

- [Python](https://www.python.org)
- [Ansible](https://ansible.com/)
- [Docker](https://docker.com)

### Configuring the environment:

Install Python dependencies (Recommend using the Python Virtualenv):

```sh
$ pip install -r requirements.txt
```

### Running tests
After the installation of python dependencies run the command below:
```sh
$ molecule test
```

## Author Information
Cloud Infrastructure Team, Linx Impulse
