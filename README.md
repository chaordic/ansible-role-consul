# Ansible Role: Consul
Installs and configure [Consul](https://www.consul.io/) on Linux.

## Requirements
- [Ansible >= 2.4](https://ansible.com/)

## Role Variables

Please look at the [defaults/main.yml](defaults/main.yml) to see all default variables.

For a simple installation and configuration, there is no mandatory variable.

## Example Playbook

```yml
---
- name: Consul server
  hosts: all
  vars:
    consul_role: server
    consul_version: 1.4.2
    ## node
    consul_domain: mydomain.consul
    ## agent
    consul_log_level: INFO
    consul_enable_syslog: true
    consul_leave_on_terminate: true
    consul_ui: true
    ## auto join
    consul_bootstrap_servers:
      - server1.domain.internal
      - server2.domain.internal

    ## DNS
    consul_dnsmasq_enable: true
    consul_dnsmasq_servers:
      - 8.8.8.8
      - 8.8.4.4

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
