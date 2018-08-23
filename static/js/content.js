$(function(){
	Dhover();//地址栏触摸事件
	createCityDom();//创建城市元素
})
//创建city元素
function createCityDom(){
	var city = ['三明','南平','莆田','厦门','福州','泉州','漳州','宁德','龙岩','平潭','将乐']
	for(var i=0;i<city.length;i++){
		$('.hide-utem').append('<li>'+city[i]+'</li>');
	}
}

//地址栏触摸事件
function Dhover(){
	var depart=getClassName('depart')[0];
	var departPoint=getClassName('depart-point')[0];
	var hideArea=getClassName('hide-area')[0];
	depart.onmouseover=function(){
		this.style.color='black';
		this.style.backgroundColor='#fff';
		departPoint.innerHTML='∨';
		hideArea.style.display='block';
	}
	depart.onmouseout=function(){
		this.style.color='#999';
		this.style.backgroundColor='rgba(110,150,0,.1)';
		departPoint.innerHTML='∧';
		hideArea.style.display='none';
	}
}

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