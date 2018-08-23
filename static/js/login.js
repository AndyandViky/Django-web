

$(function(){
    //下滑显现
    $('.login').slideDown(1000,function(){
        $('input').animate({
            opacity:1   
        },500);
    });
    djugeText();
    startShow();
})

//判断文本框是否输入正确的格式
function djugeText(){
    $('#username,.password,#email').on('blur',function(){
         var $data = $(this).val();
         if($data==""){
            $('.errorInfo').remove();
            $('.succsed').remove();
            $(this).after('<span class="errorInfo">输入不能为空!</span>')
         }
         else{
            $('.errorInfo').remove();
            $('.succsed').remove();
            $(this).after('<span class="succsed">输入成功!</span>')
         }
    })
    $('.login input[type="submit"]').on('click',function(){
        var $count = $('#username').val();
		var info="";
        var $password = $('.password').val();
        if($count=="" || $password==""){
            info = "用户名或密码不能为空！"
            animate(info);
			return false;
        }
    })
}
function animate(info){
    $('.tip-info').text(info);
    $('.tip-info').animate({
        opacity:1,
    },300,function(){
		$('.tip-info').animate({
        	opacity:0,
    	},2000) 
	}) 
}

function startShow(){
        var can=document.getElementById('canvas');
		var ctx=can.getContext('2d');
		var w=can.width=window.innerWidth;
		var h=can.height=window.innerHeight;
		window.onresize=function(){
			w=can.width=window.innerWidth;
			h=can.height=window.innerHeight;
		}
		var drops=[];
		var count=30;
		function Drop(){};

		Drop.prototype={
			init:function(){
				this.x=random(0,w);
				this.y=0;
				this.vy=random(5,6);
				this.l=random(0.4*w,0.9*h);
				this.r=1;
				this.vr=1;
				this.a=1;
				this.va=0.96;
			},
			draw:function(){
				if(this.y>this.l)
				{
					//绘制圆；
					ctx.beginPath();
					ctx.arc(this.x,this.y,this.r,0,2*Math.PI,false);
					ctx.strokeStyle="rgba(0,255,255,"+this.a+")";
					ctx.stroke();
				}else
				{
					ctx.fillStyle="#ccc";
					ctx.fillRect(this.x,this.y,1,5);
				}
				this.updata();
			},
			updata:function(){
				if(this.y<this.l)
				{
					this.y+=this.vy;
				}
				else{
					if(this.a>0.03)
					{
						this.r+=this.vr;
						if(this.r > 30 )
						{
							this.a*=this.va;
						}
					}else{
						this.init();
					}
				}
				
			}
		}
		function setDrop(){
			for(var i=0;i<count;i++)
			{
				(function(j){
					setTimeout(function(){
					var drop=new Drop();
					drop.init();
					drops.push(drop);
					},j*300);	
				})(i)
			}
		}
		setDrop();
		function move(){
			ctx.fillStyle="rgba(99,120,0,1)";
			ctx.fillRect(0,0,w,h);
			for(var i=0;i<drops.length;i++)
			{
				drops[i].draw();
			}
			requestAnimationFrame(move);//js原生经动画实现动画
		}
		move();


		function random(min,max)
		{
			var a =Math.random()*(max-min)+min;
			return a;
		}
}
