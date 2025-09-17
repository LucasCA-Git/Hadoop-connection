# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
N_SLAVES = 2

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  config.vm.define "master" do |master|
    master.vm.hostname = "master"
    master.vm.network "private_network", ip: "192.168.56.10"

    master.vm.network "forwarded_port", guest: 8088, host: 8088
    master.vm.network "forwarded_port", guest: 50070, host: 50070
    master.vm.network "forwarded_port", guest: 9081, host: 9081
    master.vm.network "forwarded_port", guest: 9080, host: 9080
  end

  (1..N_SLAVES).each do |i|
    config.vm.define "slave#{i}" do |slave|
      slave.vm.hostname = "slave#{i}"
      slave.vm.network "private_network", ip: "192.168.56.1#{i}"
    end
  end
end