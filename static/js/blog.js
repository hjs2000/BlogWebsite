// jquery返回顶部
$(function () {
    $(window).scroll(function () {
        var scrollTop = $(document).scrollTop();
        if (scrollTop >= 200) {
            $("#gotoTop").show();
        } else {
            $("#gotoTop").hide();
        }
    });
    $("#gotoTop").click(function () {
        $("html,body").animate({
                scrollTop: 0,
            },
            700
        );
    });
});

// 更换头像弹窗
$(function () {
    // 获取弹窗
    var popUp = document.getElementById('myPopUp');
    // 打开弹窗的按钮对象
    var btn = document.getElementById("imgUpdate");
    // 获取 <span> 元素，用于关闭弹窗
    var span = document.querySelector('.close-popUp');
    // 点击按钮打开弹窗
    btn.onclick = function () {
        popUp.style.display = "block";
    }
    // 点击 <span> (x), 关闭弹窗
    span.onclick = function () {
        popUp.style.display = "none";
    }
    // 在用户点击其他地方时，关闭弹窗
    window.onclick = function (event) {
        if (event.target == popUp) {
            popUp.style.display = "none";
        }
    }
});

// 鼠标点击特效
$(function () {
    //定义获取词语下标
    var a_idx = 0;
    jQuery(document).ready(function ($) {
        //点击body时触发事件
        $("body").click(function (e) {
            //需要显示的词语
            var a = new Array("富强", "民主", "文明", "和谐", "自由", "平等", "公正", "法治", "爱国", "敬业", "诚信", "友善");
            //设置词语给span标签
            var $i = $("<span/>").text(a[a_idx]);
            //下标等于原来下标+1  余 词语总数
            a_idx = (a_idx + 1) % a.length;
            //获取鼠标指针的位置，分别相对于文档的左和右边缘。获取x和y的指针坐标
            var x = e.pageX,
                y = e.pageY;
            //在鼠标的指针的位置给$i定义的span标签添加css样式
            $i.css({
                "z-index": 999999,
                "top": y - 20,
                "left": x,
                "position": "absolute",
                "font-weight": "bold",
                "font-size": "14px",
                "color": getColor()
            });
            //在body添加这个标签
            $("body").append($i);
            //animate() 方法执行 CSS 属性集的自定义动画。
            //该方法通过CSS样式将元素从一个状态改变为另一个状态。CSS属性值是逐渐改变的，这样就可以创建动画效果。详情请看http://www.w3school.com.cn/jquery/effect_animate.asp
            $i.animate({
                //将原来的位置向上移动180
                "top": y - 180,
                "opacity": 0 //1500动画的速度
            }, 1500, function () {
                //时间到了自动删除
                $i.remove();
            });
        });
    });
    // 编写一个函数，获得一个十六进制的随机颜色的字符串(例如：#ff6651)
    function getColor() {
        let newStr = ''
        let str = '1234567890ABCDEF'
        for (let i = 0; i < 6; i++) {

            newStr += str.charAt(Math.floor(Math.random() * 16))
        }
        return '#' + newStr
    }
});