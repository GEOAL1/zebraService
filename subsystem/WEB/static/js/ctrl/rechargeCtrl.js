/**
 * Created by eric on 6/2/15.
 */

app.controller("rechargeController", function ($scope, $http, userService) {

        $scope.recharge  = function(rechargeAmount,$event) {
            if ($scope.check_pay_type === undefined) {
                alert("请选择充值类型")
                return;
            }
            userService.recharge(rechargeAmount, function (statue, data) {
                    if(statue == 0) {
                        alert($scope.check_pay_type + "充值成功")
                    }else{
                        alert($scope.check_pay_type+  "充值失败")
                    }
                })
        }
})



