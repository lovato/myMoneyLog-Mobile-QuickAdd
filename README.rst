================
myMoneyLog Mobile QuickAdd
================

:Info: A mini website that can be used by remote devices to add data to the offline myMoneyLog software
:Author: Marco Lovato (http://github.com/lovato)

Adds a new feature to myMoneyLog ( http://nishimura.eti.br/blog/mymoneylog/ ). Thanks to: Ricardo Nishimura

Current Travis Status:

.. image:: https://secure.travis-ci.org/lovato/myMoneyLog-Mobile-QuickAdd.png?branch=master
  :target: http://travis-ci.org/lovato/myMoneyLog-Mobile-QuickAdd

.. contents::

Installation
============

My scenario to make this work was to install myMoneyLog on my Synology device, and share that folder with my Windows workstations.
Thats because me and my wife use the same database of myMoneyLog.
In this same Synology box I am running Python, and opened access to external world for a specific port.
Other possibility is to host this solution somewhere, and then achieve to sync "somewhere"/data.html file with your diskstation or single workstation.

Running
=======

For a Synology Diskstation, its basically to call "nohup python main.py&"