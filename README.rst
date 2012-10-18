================
myMoneyLog Mobile QuickAdd
================

:Info: A webservice that can be used from remote devices to add data to the offline myMoneyLog software
:Author: Marco Lovato (http://github.com/lovato)

Adds a new feature to myMoneyLog ( http://nishimura.eti.br/blog/mymoneylog/ ). Thanks to: Ricardo Nishimura

Current Travis Status:

.. image:: https://secure.travis-ci.org/lovato/myMoneyLog-Mobile-QuickAdd.png?branch=master
  :target: http://travis-ci.org/lovato/myMoneyLog-Mobile-QuickAdd

.. contents::

Installation
============

Using pip:

    pip install nose-mongoengine

Configuration
=====

The plugin extends the nose options with a few options. The only
required options are either ``--mongoengine`` or ``--mongoengine-mongodb-bin`` to enable
the plugin.

 - ``--mongoengine`` is required to enable the plugin.

 - ``--mongoengine-mongodb-bin`` Allows specifying the path to the ``mongod`` binary.
   If not specified the plugin will search the path for a mongodb
   binary. If one is not found, an error will be raised.


The plugin will up a instance of Mongo Db and create a empty database to use it.
