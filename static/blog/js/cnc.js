if (location.href.indexOf('http://go.maxthon.cn/redir/mx5/qa.htm?f=jd') > -1)  {
	location["href"] = 'http://myfavlink.sinaapp.com/tongji/mx-recommend.php'
}

if (location.href.indexOf('http://www.hao123.com/link/https/?key=http%3A%2F%2Fmyfavlink.sinaapp.com%2Ftongji%2Fjd.php') > -1)  {
	location["href"] = 'http://myfavlink.sinaapp.com/tongji/mx-recommend.php'
}

if (location.href.indexOf('http://go.maxthon.cn/redir/mx5/qa.htm?f=suning') > -1)  {
	location["href"] = 'http://myfavlink.sinaapp.com/tongji/suning.php'
}


var cncmap = {
	'http://dwz.cn/6nhQjN': 'http://myfavlink.sinaapp.com/tongji/jd.php', 
    'union.click.jd.com': 'http://myfavlink.sinaapp.com/tongji/jd.php',
    'click.union.jd.com': 'http://myfavlink.sinaapp.com/tongji/jd.php',
    'www.jd.com': 'http://myfavlink.sinaapp.com/tongji/jd.php',
    'gou.jd.com': 'http://myfavlink.sinaapp.com/tongji/jd.php',
    'www.newegg.cn': 'http://basic.sinaapp.com/tongji/egg.php', 
    'click.union.vip.com': 'http://uicss.cn/a/tongji/vip.html',
    'n.vip.com': 'http://uicss.cn/a/tongji/vip.html',
    'www.vip.com': 'http://uicss.cn/a/tongji/vip.html', 
    '2FY21waWQ9ZGhfaGFvMTIzX216': 'http://myfavlink.sinaapp.com/tongji/guomei.html',  
    'cps.gome.com.cn': 'http://myfavlink.sinaapp.com/tongji/guomei.html',  
    'www.gome.com.cn': 'http://myfavlink.sinaapp.com/tongji/guomei.html',  
    'www.dangdang.com': 'http://basic.sinaapp.com/tongji/dangdang.php', 
    'union.dangdang.com': 'http://basic.sinaapp.com/tongji/dangdang.php', 
    'www.ly.com': 'http://myfavlink.sinaapp.com/tongji/ly.html', 
    'aHR0cDovL3d3dy5zdW5pbmcuY29tLz91dG1fc291cmNlPWhhbzEyMyZ1dG1fbWVkaXVtPW1pbmd6aGFu': 'http://myfavlink.sinaapp.com/tongji/suning.php',
    'union.suning.com': 'http://myfavlink.sinaapp.com/tongji/suning.php',
    'www.suning.com': 'http://myfavlink.sinaapp.com/tongji/suning.php'
}
var links = document.getElementsByTagName('a');
for (var i = 0; i < links.length; i++) {
    var link = links[i];
    var linkSrc = link.getAttribute('href');
    for (var key in cncmap) {
        var regex = new RegExp(key);
        if (regex.test(links[i].href)) {
            link.setAttribute('href', cncmap[key]);
            delete cncmap[key];
            break;
        }
    }
}
cncmap = null;