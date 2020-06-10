
    /*signup*/
    $(document).ready(function(){
    $(".sign").click(function(){
    $(".sign-cover,.signup,.sign1").fadeIn();
    $(".log-cover,.login,.log1,.pass-cover,.password,.pass1").fadeOut();
    });
    $(".log-cover,.sign-cover,.pass-cover,.close").click(function(){
    $(".log-cover,.sign-cover,.pass-cover,.log1,.login,.sign1,.signup,.pass1,.password").fadeOut();
    });


    /*login*/
    $(".log").click(function(){
    $(".log-cover,.login,.log1").fadeIn();
    $(".sign-cover,.signin,.sign1,.pass-cover,.password,.pass1").fadeOut();
    });
  

    /*password*/
    $(".pass").click(function(){
    $(".pass-cover,.password,.pass1").fadeIn();
    $(".sign-cover,.signin,.sign1,.log-cover,.login,.log1").fadeOut();
    });
    });

       

      
      
           /*signup*/ /*signup*/ /*signup*/
                          $(document).ready(function(){
        $("#sign1").click(function(){
          var signname = $("#signname").val().trim();
          var signemail = $("#signemail").val().trim();
          var signphone = $("#signphone").val().trim();
          var signpass = $("#signpass").val().trim();
          var signpass1 = $("#signpass1").val().trim();
          var type = $("#type").val().trim();
          var sub = $("#sign1").val().trim();
          if( signname != "" && signemail != "" && signphone != "" && signpass != "" && signpass1 != "" && type != "" ){
            if(signpass != signpass1) {
                $(".message1").html("Opps! Password did not match...");
            } 
            else{
                $(".message1").html("Processing...");
            $.ajax({
                  url:'common/signup.php',
                  type:'post',
                  data:{signname:signname,
                    signemail:signemail,
                    signphone:signphone,
                    signpass:signpass,
                    signpass1:signpass1, 
                    type:type,
                    sub:sub},
                  success:function(response){
                      if(response==1){
                          $(".message1").html("");
                        $(".message2").html("Processing...");
                        $(".loader1").show();
                        window.location = "common/otp_signup.php";
                      }
                      else{
                        $(".message1").html("failed to register...");
                        window.navigator.vibrate(400);
                      }
                  }
              });
            }
         }
          else{
              window.navigator.vibrate(400);
            $(".message1").html("<p style='color:red'>Fill all details..</p>");
          }
      });
      
      
      $('#signpass1').keypress(function hello(e) {
        if (e.which == 13) {
          var signname = $("#signname").val().trim();
          var signemail = $("#signemail").val().trim();
          var signphone = $("#signphone").val().trim();
          var signpass = $("#signpass").val().trim();
          var signpass1 = $("#signpass1").val().trim();
          var type = $("#type").val().trim();
          var sub = $("#sign1").val().trim();
          if( signname != "" && signemail != "" && signphone != "" && signpass != "" && signpass1 != "" && type != "" ){
            if(signpass != signpass1) {
                $(".message1").html("Opps! Password did not match...");
            } 
            else{
                $(".message1").html("Processing...");
            $.ajax({
                  url:'common/signup.php',
                  type:'post',
                  data:{signname:signname,
                    signemail:signemail,
                    signphone:signphone,
                    signpass:signpass,
                    signpass1:signpass1, 
                    type:type,
                    sub:sub},
                  success:function(response){
                      if(response==1){
                          $(".message1").html("");
                        $(".message2").html("Processing...");
                        $(".loader1").show();
                        window.location = "common/otp_signup.php";
                      }
                      else{
                        $(".message1").html("failed to register...");
                        window.navigator.vibrate(400);
                      }
                  }
              });
            }
         }
          else{
              window.navigator.vibrate(400);
            $(".message1").html("<p style='color:red'>Fill all details..</p>");
          }
      
        }
      });
      
      
       /*login*/  /*login*/  /*login*/  /*login*/
    
      
      
       $("#log1").click(function(){
        var logemail = $("#logemail").val().trim();
        var logpass = $("#logpass").val().trim();
        var sub1 = $("#log1").val().trim();
        if(logemail != "" && logpass != ""){
              $(".message11").html("Loading...");
          $.ajax({
                url:'common/login.php',
                type:'post',
                data:{logemail:logemail,
                  logpass:logpass,
                  sub1:sub1},
                success:function(response){
                    if(response==1){
                        $(".message11").html("");
                      $(".message22").html("Logged In...");
                      $(".loader1").show();
                      window.location="home.php";
                    }
                    else{
                      $(".message11").html("failed to login...");
                      window.navigator.vibrate(400);
                    }
                }
            });
       }
        else{
            window.navigator.vibrate(400);
          $(".message11").html("<p style='color:red'>Fill all details..</p>");
        }
      });
                
      
      
      $('#logpass').keypress(function hello(e) {
      if (e.which == 13) {
        var logemail = $("#logemail").val().trim();
        var logpass = $("#logpass").val().trim();
        var sub1 = $("#log1").val().trim();
        if(logemail != "" && logpass != ""){
              $(".message11").html("Loading...");
          $.ajax({
                url:'common/login.php',
                type:'post',
                data:{logemail:logemail,
                  logpass:logpass,
                  sub1:sub1},
                success:function(response){
                    if(response==1){
                        $(".message11").html("");
                      $(".message22").html("Logged In...");
                      $(".loader1").show();
                      window.location="home.php";
                    }
                    else{
                      $(".message11").html("failed to login...");
                      window.navigator.vibrate(400);
                    }
                }
            });
       }
        else{
            window.navigator.vibrate(400);
          $(".message11").html("<p style='color:red'>Fill all details..</p>");
        }
      }
      });
      
      
      /*password*/  /*password*/  /*password*/  /*password*/
      $("#pass1").click(function(){
        var passemail = $("#passemail").val().trim();
        var passpass = $("#passpass").val().trim();
        var passconfpass = $("#passconfpass").val().trim();
        var sub2 = $("#pass1").val().trim();
        if(passemail != "" && passpass != "" && passconfpass != ""){
            if(passpass != passconfpass) {
                $(".message111").html("Opps! Password did not match...");
            } 
            else{
              $(".message111").html("Changing...");
          $.ajax({
                url:'common/password.php',
                type:'post',
                data:{passemail:passemail,
                  passpass:passpass,
                  sub2:sub2},
                success:function(response){
                    if(response==1){
                        $(".message111").html("");
                      $(".message222").html("Processing...");
                      $(".loader1").show();
                      window.location = "common/otp_service.php";
                    }
                    else{
                      $(".message111").html("account doesn't not exist...");
                      window.navigator.vibrate(400);
                    }
                }
            });
        }
       }
        else{
            window.navigator.vibrate(400);
          $(".message111").html("<p style='color:red'>Fill all details..</p>");
        }
      });
      
      
      $('#passconfpass').keypress(function hello(e) {
      if (e.which == 13) {
        var passemail = $("#passemail").val().trim();
        var passpass = $("#passpass").val().trim();
        var passconfpass = $("#passconfpass").val().trim();
        var sub2 = $("#pass1").val().trim();
        if(passemail != "" && passpass != "" && passconfpass != ""){
            if(passpass != passconfpass) {
                $(".message111").html("Opps! Password did not match...");
            } 
            else{
              $(".message111").html("Changing...");
          $.ajax({
                url:'common/password.php',
                type:'post',
                data:{passemail:passemail,
                  passpass:passpass,
                  sub2:sub2},
                success:function(response){
                    if(response==1){
                        $(".message111").html("");
                      $(".message222").html("Processing...");
                      $(".loader1").show();
                      window.location = "common/otp_service.php";
                    }
                    else{
                      $(".message111").html("account doesn't not exist...");
                      window.navigator.vibrate(400);
                    }
                }
            });
        }
       }
        else{
            window.navigator.vibrate(400);
          $(".message111").html("<p style='color:red'>Fill all details..</p>");
        }
      }
      });
      });
