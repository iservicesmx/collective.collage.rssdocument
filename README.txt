Introduction
============
This is a Add-On product for Products.Collage. The purpose of collective.collage.rssdocument
is to display RSSDocuments inside a Collage.

RSSDocument lives inside iservices.rssdocument. It is a dynamic RSS content-type
for plone. It embedds a few items from a RSS feed in the main_content area using
the zRSSFeed jQuery plugin.


Usage
-----

Install this product using Buildout, or a similar method, and then start up
your Plone instance.  The ZCML configuration will automatically get picked up
and register these additional views for your Collage content.  

You should install ``iservices.rssdocument`` on your site in order for
this Collage view to be useful.  Then insert or link a RSSDocument inside your
collage. Don't forget to publish your RSSDocument

Credits
-------

zRSSFeed jQuery Plugin has been made by Zazar Ltd. All rights reserved.
http://www.zazar.net/developers/zrssfeed/


Noe Nieto <noe@iservices.com.mx>

iservices.rssdocument has been made by iServices de Mexico.


