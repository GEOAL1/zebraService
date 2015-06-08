app.controller("registerController", function ($scope, $http, userService) {
    $scope.countdown = 0
    $scope.sendCode_show=true

    $scope.sendCode = function (phone) {
        $scope.countdown = 30;
        $scope.myTime = setInterval(function() {
            $scope.countdown--;
            if($scope.countdown <= 0) {
                $scope.sendCode_show=true
                clearInterval($scope.myTime)
            }else{
                $scope.sendCode_show=false

            }
            $scope.$digest(); // 通知视图模型的变化
        }, 1000);
        $http({
            method:"GET",
            url:'/wx/send/phoneCode?ph='+phone
        }).success(function(data,status,headers,config){
            if(data.errorCode===0) {
                console.log("send success");
            }
            alert(data.errorCode);
        }).error(function(data,status,headers,config){
            console.log("send error")
        })
    }

    $scope.signupForm = userService.register

})



