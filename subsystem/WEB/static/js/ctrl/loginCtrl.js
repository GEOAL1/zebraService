app.controller("loginController", function ($scope, $http, userService) {
    $scope.regisiterUrl = "/static/reg.html"
    $scope.login = userService.login
})