


window.onload=function(){
	clikSearchEvent();
}

$.getJSON("/country/get_ajax_tourist/春季",function(data){
	createScenicSportDom(data);
	ConditionSortEvent(data);//根据条件排序
})

//创建景点元素
function createScenicSportDom(arr){
	var len = arr.length;
	var scenicSport=document.querySelector('.scenicSport');
	for(var i=0;i<len;i++)
	{
		var li = createEl('li');
		var imgBox=createEl('div','class','imgBox');
		var imga = createEl('a',"href",arr[i].id);
		var img = createEl('img','src',"/"+arr[i].image,'class','imgBox1');//
		imga.appendChild(img);
		imgBox.appendChild(imga);
		li.appendChild(imgBox);
		var imgDecritionBox=createEl('div','class','img-decritionBox');
		var h4=createEl('h4','class','imgBox2');
		h4.innerHTML=arr[i].name;
		imgDecritionBox.appendChild(h4);
		var persons=createEl('div','class','persons');
		var img1=createEl('img','src','/static/images/星星.png');
		persons.appendChild(img1);
		var p=createEl('p');
		p.innerHTML='人气：';
		var span = createEl('span','class','count');
		span.innerHTML=arr[i].person;
		p.appendChild(span);
		persons.appendChild(p);
		imgDecritionBox.appendChild(persons);
		var p1= createEl('p','class','decrition');
		p1.innerHTML=arr[i].detail;
		var a = createEl('a','href',arr[i].href);
		a.innerHTML='[详情]';
		p1.appendChild(a);
		imgDecritionBox.appendChild(p1);
		var price= createEl('div','class','price');
		price.innerHTML='￥ '+arr[i].price;
		imgDecritionBox.appendChild(price);
		var rank=createEl('div','class','rank');
		rank.innerHTML=arr[i].rank;
		imgDecritionBox.appendChild(rank);
		li.appendChild(imgDecritionBox);
		scenicSport.appendChild(li);
	}
}

//点击搜索事件
function clikSearchEvent(){
	var text=document.getElementById('t');
	var button=document.getElementById('b');
	var header=document.getElementById('head');
	button.onclick=function(){
		$('.scenicSport>li').remove();
		changeData(text,button,header);
	}
	text.onkeydown=function(e){
		if(e.keyCode==13)
		{
			$('.scenicSport>li').remove();
			changeData(text,button,header);
			return false;
		}
	}
}
//根据搜索改变数据
function changeData(text,button,header){
	var url = "/country/get_ajax_tourist/";
	if(text.value.indexOf("夏")==0){
		url+="夏季";
		changeBg(text,button,header,'green','春季/秋季/冬季');
		$.getJSON(url,function(data){
			createScenicSportDom(data);
			ConditionSortEvent(data);//根据条件排序
		});
		$('.condition-sort>li').eq(0).addClass('bg').siblings().removeClass('bg');
	}
	else if(text.value.indexOf("秋")==0){
		url+="秋季";
		changeBg(text,button,header,'#eaea4f','春季/夏季/冬季');
		$.getJSON(url,function(data){
			createScenicSportDom(data);
			ConditionSortEvent(data);//根据条件排序
		});
		$('.condition-sort>li').eq(0).addClass('bg').siblings().removeClass('bg');
	}
	else if(text.value.indexOf("冬")==0){
		url+="冬季";
		changeBg(text,button,header,'#ccc','春季/夏季/秋季');
		$.getJSON(url,function(data){
			createScenicSportDom(data);
			ConditionSortEvent(data);//根据条件排序
		});
		$('.condition-sort>li').eq(0).addClass('bg').siblings().removeClass('bg');
	}
	else if(text.value.indexOf("春")==0){
		location.reload();	
	}
	else{
		location.href="/country/404/";	
	}
}
//更改皮肤
function changeBg(t,b,h,color,attr){
	t.style.borderColor=color;
	b.style.borderColor=color;
	b.style.backgroundColor=color;
	h.style.borderColor=color;
	t.setAttribute('placeholder',attr)
}


//点击排序
function ConditionSortEvent(data){
	$('.condition-sort>li').on('click',function(){
		var i=$(this).index();
		$('.scenicSport>li').remove();
		Sort(data,data.length,i);
	})
}
//排序
function Sort(arr,len,index){
	$('.condition-sort>li').eq(index).addClass('bg').siblings().removeClass('bg');
	if(index==0)
	{
		for(var i=0;i<len-1;i++)
		{
			var k=i;
			for(var j=k;j<len;j++)
			{
				if(arr[j].id<arr[k].id)k=j;
			}
			var temp=arr[i];
			arr[i]=arr[k];
			arr[k]=temp;
		}
		createScenicSportDom(arr);
	}
	else if(index==1)
	{
		for(var i=0;i<len-1;i++)
		{
			var k=i;
			for(var j=k;j<len;j++)
			{
				if(arr[j].person>arr[k].person)k=j;
			}
			var temp=arr[i];
			arr[i]=arr[k];
			arr[k]=temp;
		}
		createScenicSportDom(arr);
	}
	else if(index==2)
	{
		for(var i=0;i<len-1;i++)
		{
			var k=i;
			for(var j=k;j<len;j++)
			{
				if(arr[j].price<arr[k].price)k=j;
			}
			var temp=arr[i];
			arr[i]=arr[k];
			arr[k]=temp;
		}
		createScenicSportDom(arr);
	}
}
//封装函数js生成元素
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


//封装函数（以类名获取元素）	
function getClassName(n){
	var result=[];
	var arr=document.getElementsByTagName('*');
	for(var i=0;i<arr.length;i++)
	{
		if(arr[i].className==n)
		{
			result.push(arr[i]);
		}
	}
	return result;
}