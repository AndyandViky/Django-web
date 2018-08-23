

window.onload=function(){
	//创建page元素
	createPageDom();
	changeData();
}
//模拟数据交互
$.getJSON("/country/get_btCountry/1",function(data){
	//创建主题元素li
	createLiDom(data);
});
function changeData(){
	//page元素点击替换数据渲染页面
	$("#page>li").on('click',function(){
		var index=$(this).index();
		var ids = parseInt($('.colorBg').text());
		if(index==0)
		{	
			if(ids==1) index=1;
			else index = ids-1;
		}
		else if(index==4)
		{
			if(ids==3) index=3;
			else index = parseInt(ids+1);
		}
		var url = "/country/get_btCountry/"+index;
		$.getJSON(url,function(data){
			for(var i=0;i<data.length;i++)
			{
				$('.Title').remove();
				$('.bt-utem').remove();
				createLiDom(data);
			}
			$("#page>li").eq(index).addClass('colorBg').siblings().removeClass('colorBg');	
		document.body.scrollTop =0; 
		})
	});
}
//创建主题li元素
function createLiDom(data){
	var main =document.getElementById("main");
	var title=createEl("div","class","Title");
	var h1=createEl("h1");
	h1.innerHTML="最美乡村";
	title.appendChild(h1);
	$(main).prepend(title);
	var ul = createEl("ul","class","bt-utem");
	for(var i=0;i<data.length;i++)
	{	
		var li =createEl("li");
		var CountryBox=createEl("div","class","CountryBox");
		var CountryName=createEl("h2","class","CountryName");
		CountryName.innerHTML=data[i].name;
		CountryBox.appendChild(CountryName);
		var imgBox=createEl("div","class","imgBox");
		var a = createEl("a","href",data[i].id);
		var img = createEl("img","src","/"+data[i].image);
		a.appendChild(img);
		imgBox.appendChild(a);
		CountryBox.appendChild(imgBox);	
		var decritionBox=createEl("div","class","decrition");
		var p1 = createEl("p");
		p1.innerHTML=data[i].detail;
		decritionBox.appendChild(p1);
		CountryBox.appendChild(decritionBox);
		li.appendChild(CountryBox);
		ul.appendChild(li);
	}
	$(title).after(ul);
}
//创建page元素
function createPageDom(){
	var main =document.getElementById("main");
	var ul = createEl("ul","id","page");
	/*$.getJSON("/country/get_btCountry/0",function(data){
		var len=2;
		if(data.length%6==0){
			len=parseInt(len+data.length/6);
		}
		else{
			len=parseInt(data.length/6+3);
		}*/
		//创建主题元素li
		var len = 5;
		for(var i=0;i<len;i++){
			var li = createEl("li");
			if(i==0) li.innerHTML="上一页";
			else if(i>0 && i<len-1){
				li.innerHTML=i;
			}
			else li.innerHTML="下一页";
			ul.appendChild(li);
		}
	//});		
	main.appendChild(ul);
	$('#page>li').eq(1).addClass('colorBg');
}


//封装函数js生成代码
function createEl(el){
	var len =arguments.length;
	if(len==1)
	{
		var el=document.createElement(el);
	}
	else if(len==3)
	{
		var attrName=arguments[1];
		var attr= arguments[2];
		var el=document.createElement(el);
		el.setAttribute(attrName,attr);
	}
	else if(len==5)
	{
		var attrName1=arguments[1];
		var attr1= arguments[2];
		var attrName2=arguments[3];
		var attr2= arguments[4];
		var el=document.createElement(el);
		el.setAttribute(attrName1,attr1);
		el.setAttribute(attrName2,attr2);
	}
	return el;
}

