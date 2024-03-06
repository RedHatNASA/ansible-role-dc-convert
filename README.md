ansible-role-dc-convert
=========

A role for converting all found OpenShift DeploymentConfig objects to Deployment yaml files.

Requirements
------------
collection:

* kubernetes.core


Role Variables
--------------
By default it will attempt a environment lookup for the following environment variables:

    K8S_AUTH_API_KEY
    K8S_AUTH_HOST

If those are not defined, it will use the following role variables:

    k8s_api_host: https://api.example.com:6443
    k8s_api_key: sha256~aBcF6Fzm53A2lnTbWxO0F97Bz678InIvfcteslLLwZc

You can also specify the directory to save the converted yaml files:

    yaml_save_dir: /home/my_user

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-dc-convert

License
-------

MIT/BSD

Author Information
------------------
filter_plugin based on the work done by [underguiz](https://github.com/underguiz) and the gist found [here](https://gist.github.com/underguiz/3f61eed7942bfb221696be6019da0d22).

This role was created by [Michael Tipton](https://ibeta.org).
