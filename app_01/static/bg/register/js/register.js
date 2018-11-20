$(function(){
    $('#btn').click(function(){
          var email = $("#email").val();
          var pwd = $("#pwd").val();
          var confirm_pwd = $("#pwd_confirm").val();

          if(email.length < 4){
              alert("邮箱不正确");
          }

          if (pwd.length < 3){
              alert('密码太短了');
          }

          if(pwd != confirm_pwd){
              alert("两次输入的密码不正确");
          }

          $.ajax({
              url:'/apis_v1/register',
              method:'post',
              data:{
                  email:email,
                  pwd:md5(pwd),
                  confirm_pwd:md5(confirm_pwd),
              },
              success:function (result) {
                    if(result.code == 1){
                        window.open(result.data,target='_self');
                    }else{
                        alert(result.msg);
                    }
              },
              error:function (result) {

              },
              complete:function(res){

              },
          });
    })
});
