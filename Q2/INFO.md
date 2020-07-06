
Host information:
   Static hostname: labhost42
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 24d060dfeaa84315ab9b337fce98b2e6
           Boot ID: 1c5dbdbbfbdc4251b4bfdaff552a1437
    Virtualization: vmware
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.el7.x86_64
      Architecture: x86-64
IP Address: 192.168.232.42


Packages installed:
telnet-0.17-64.el7.x86_64
python-pycurl-7.19.0-19.el7.x86_64
MySQL-python-1.2.5-1.el7.x86_64
mysql-community-server-8.0.20-1.el7.x86_64
mysql-community-libs-compat-8.0.20-1.el7.x86_64
mysql-community-libs-8.0.20-1.el7.x86_64
mysql-community-common-8.0.20-1.el7.x86_64
mysql-community-client-8.0.20-1.el7.x86_64
mysql80-community-release-el7-1.noarch
libcurl-7.29.0-51.el7.x86_64
java-1.8.0-openjdk-1.8.0.252.b09-2.el7_8.x86_64
httpd-tools-2.4.6-93.el7.centos.x86_64
httpd-2.4.6-93.el7.centos.x86_64
curl-7.29.0-51.el7.x86_64


Active firewall details:
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: ens33
  sources: 
  services: ssh dhcpv6-client http
  ports: 8080/tcp 3306/tcp 6443/tcp 2379-2380/tcp 10250/tcp 10251/tcp 10252/tcp 10255/tcp 30000-32767/tcp 6783/tcp
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
	


Server:		192.168.232.2
Address:	192.168.232.2#53

Non-authoritative answer:
Name:	www.google.com
Address: 172.217.194.104
Name:	www.google.com
Address: 172.217.194.103
Name:	www.google.com
Address: 172.217.194.147
Name:	www.google.com
Address: 172.217.194.105
Name:	www.google.com
Address: 172.217.194.99
Name:	www.google.com
Address: 172.217.194.106



● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2020-07-07 00:45:44 +08; 16min ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 64495 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
   CGroup: /system.slice/httpd.service
           ├─64495 /usr/sbin/httpd -DFOREGROUND
           ├─64496 /usr/sbin/httpd -DFOREGROUND
           ├─64497 /usr/sbin/httpd -DFOREGROUND
           ├─64498 /usr/sbin/httpd -DFOREGROUND
           ├─64499 /usr/sbin/httpd -DFOREGROUND
           ├─64500 /usr/sbin/httpd -DFOREGROUND
           └─66273 /usr/sbin/httpd -DFOREGROUND

Jul 07 00:45:44 labhost42 systemd[1]: Starting The Apache HTTP Server...
Jul 07 00:45:44 labhost42 httpd[64495]: AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 192.168.232.42. Set the 'ServerName' directive globally to suppress this message
Jul 07 00:45:44 labhost42 systemd[1]: Started The Apache HTTP Server.

● tomcat.service - Tomcat
   Loaded: loaded (/etc/systemd/system/tomcat.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2020-07-05 13:56:36 +08; 1 day 11h ago
 Main PID: 7197 (java)
   CGroup: /system.slice/tomcat.service
           └─7197 /usr/lib/jvm/jre/bin/java -Djava.util.logging.config.file=/usr/share/tomcat/apache-tomcat-9.0.30/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djava.awt.headless=true -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 -Dignore.endorsed.dirs= -classpath /usr/share/tomcat/apache-tomcat-9.0.30/bin/bootstrap.jar:/usr/share/tomcat/apache-tomcat-9.0.30/bin/tomcat-juli.jar -Dcatalina.base=/usr/share/tomcat/apache-tomcat-9.0.30 -Dcatalina.home=/usr/share/tomcat/apache-tomcat-9.0.30 -Djava.io.tmpdir=/usr/share/tomcat/apache-tomcat-9.0.30/temp org.apache.catalina.startup.Bootstrap start

Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.

● mysqld.service - MySQL Server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2020-07-05 13:56:39 +08; 1 day 11h ago
     Docs: man:mysqld(8)
           http://dev.mysql.com/doc/refman/en/using-systemd.html
 Main PID: 7572 (mysqld)
   Status: "Server is operational"
   CGroup: /system.slice/mysqld.service
           └─7572 /usr/sbin/mysqld

Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.


Curl to www.google.com:
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-SG"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="yUKc0VunjLkV3acj+2FsRg==">(function(){window.google={kEI:'AVoDX6L5NaDSz7sPnI2gsAU',kEXPI:'0,202123,3,4,32,1151584,5663,730,224,5105,206,2415,701,88,10,1226,364,926,573,612,91,114,383,246,5,1184,170,648,514,166,5,361,2184,222,12,113,73,110,6,3,995,55,40,51,192,112,71,93,1121740,1197695,454,329118,1294,12383,4855,32691,15248,867,28684,9188,8384,4859,1361,9291,3022,2821,1924,1848,4720,4460,2,1811,4020,978,7931,5297,2054,920,873,1217,2983,6422,11306,3222,234,4283,2777,919,2279,8,85,2709,1593,1279,2212,239,291,149,1103,840,517,1522,157,4101,312,1136,3,2669,1839,184,1920,377,1947,2229,93,328,1284,16,445,2482,2247,473,1339,1787,3227,2845,7,5599,469,6286,4454,642,2449,2459,1226,1742,3654,1275,108,3407,908,2,941,2614,2397,1386,4949,1975,1337,1098,3,346,230,970,865,373,3545,707,148,189,3312,503,1,1985,158,1,2092,3943,1039,101,651,4,1528,17,358,919,1010,1236,271,874,405,1839,21,177,69,1849,331,503,41,297,917,9,43,214,1111,91,1424,460,117,1226,212,1140,629,794,1504,935,1330,86,3,610,883,1787,1426,69,24,69,1564,958,579,1220,727,285,939,2,2,360,468,672,981,987,2,243,32,46,169,106,325,2,3,81,108,91,172,2281,501,71,68,262,239,4,867,278,5,203,7,71,469,55,23,259,171,2,140,31,1041,261,353,99,34,138,781,48,478,5795082,3481,8798434,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,879,9,305,2919,21,12,25,21,2,34,11,55,24,23961280,2682732',kBL:'4qAS'};google.sn='webhp';google.kHL='en-SG';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){ document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this); var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important} </style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="yUKc0VunjLkV3acj+2FsRg=="></script></head><body bgcolor="#fff"><script nonce="yUKc0VunjLkV3acj+2FsRg==">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;} if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();} } })();</script><div id="mngb"><div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="http://www.google.com.sg/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="http://maps.google.com.sg/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="http://www.youtube.com/?gl=SG&tab=w1">YouTube</a> <a class=gb1 href="http://news.google.com.sg/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com.sg/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com.sg/history/optout?hl=en" class=gb4>Web History</a> | <a href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.com/" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div></div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-SG" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000" autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="I'm Feeling Lucky" name="btnI" type="submit"><script nonce="yUKc0VunjLkV3acj+2FsRg==">(function(){var id='tsuid1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;} else top.location='/doodles/';};})();</script><input value="AINFCbYAAAAAXwNoEf_Vd0FZgj9sO8fX2E6jCecnHn3a" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-SG&amp;authuser=0">Advanced search</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="yUKc0VunjLkV3acj+2FsRg==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google offered in: <a href="http://www.google.com/setprefs?sig=0_qtwFoMRtaZrhNJAGPmNqOVgy0lk%3D&amp;hl=zh-CN&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwji_ZyhjrnqAhUg6XMBHZwGCFYQ2ZgBCAU">&#20013;&#25991;(&#31616;&#20307;)</a> <a href="http://www.google.com/setprefs?sig=0_qtwFoMRtaZrhNJAGPmNqOVgy0lk%3D&amp;hl=ms&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwji_ZyhjrnqAhUg6XMBHZwGCFYQ2ZgBCAY">Melayu</a> <a href="http://www.google.com/setprefs?sig=0_qtwFoMRtaZrhNJAGPmNqOVgy0lk%3D&amp;hl=ta&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwji_ZyhjrnqAhUg6XMBHZwGCFYQ2ZgBCAc">&#2980;&#2990;&#3007;&#2996;&#3021;</a> </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising�Programs</a><a href="http://www.google.com.sg/intl/en/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a><a href="http://www.google.com/setprefdomain?prefdom=SG&amp;prev=http://www.google.com.sg/&amp;sig=K_Z26s0RIFG_SKkyVh_AKxqMKQOWQ%3D">Google.com.sg</a></div></div><p style="font-size:8pt;color:#767676">&copy; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="yUKc0VunjLkV3acj+2FsRg==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u='/xjs/_/js/k\x3dxjs.hp.en.rgZ6CA4tLZ8.O/m\x3dsb_he,d/am\x3dAE-wOQ/d\x3d1/rs\x3dACT90oFCqzp63wk29hflpOwl6XzMk2ydsA'; setTimeout(function(){var b=document;var a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu='/xjs/_/js/k\x3dxjs.hp.en.rgZ6CA4tLZ8.O/m\x3dsb_he,d/am\x3dAE-wOQ/d\x3d1/rs\x3dACT90oFCqzp63wk29hflpOwl6XzMk2ydsA';})();function _DumpException(e){throw e;} function _F_installCss(c){} (function(){google.jl={dw:false,em:[],emw:false,lls:'default',pdt:0,snet:true,uwp:true};})();(function(){var pmc='{\x22d\x22:{},\x22sb_he\x22:{\x22agen\x22:true,\x22cgen\x22:true,\x22client\x22:\x22heirloom-hp\x22,\x22dh\x22:true,\x22dhqt\x22:true,\x22ds\x22:\x22\x22,\x22ffql\x22:\x22en\x22,\x22fl\x22:true,\x22host\x22:\x22google.com\x22,\x22isbh\x22:28,\x22jsonp\x22:true,\x22msgs\x22:{\x22cibl\x22:\x22Clear Search\x22,\x22dym\x22:\x22Did you mean:\x22,\x22lcky\x22:\x22I\\u0026#39;m Feeling Lucky\x22,\x22lml\x22:\x22Learn more\x22,\x22oskt\x22:\x22Input tools\x22,\x22psrc\x22:\x22This search was removed from your \\u003Ca href\x3d\\\x22/history\\\x22\\u003EWeb History\\u003C/a\\u003E\x22,\x22psrl\x22:\x22Remove\x22,\x22sbit\x22:\x22Search by image\x22,\x22srch\x22:\x22Google Search\x22},\x22ovr\x22:{},\x22pq\x22:\x22\x22,\x22refpd\x22:true,\x22rfs\x22:[],\x22sbpl\x22:16,\x22sbpr\x22:16,\x22scd\x22:10,\x22stok\x22:\x22UfXrCEOh4rLK5ekGjAj_Uz8cGuk\x22,\x22uhde\x22:false}}';google.pmc=JSON.parse(pmc);})();</script> </body></html>
