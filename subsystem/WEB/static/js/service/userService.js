app.service('userService', function ($rootScope, $http) {
    var sendCmd = function (url, method, data, callback) {
        var http_config = {};
        if (method == "GET") {
            http_config = {
                method: "GET",
                url: url,
                params: data,
                timeout: 5000,
            }
        } else {
            http_config = {
                method: "POST",
                url: url,
                data: $.param(data),
                timeout: 5000,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            }
        }

        $http(http_config).success(function (data, status, headers, config) {

            if (data.errorCode != 0) {
                console.log(data.errorCode + " : " + data.er)
            }
            callback(data.errorCode, data)
        }).error(function (data, status, headers, config) {

            if (status == 403) {
                alert("登录超时，请重新登录")
                window.location.href = "/static/login.html"
            }

            callback(-1, {errorCode: -1, errorMeg: "服务器忙，请稍后再试"})
        });
    };

    var service = {
        getUserInfo: function (cb) {
            sendCmd("/wx/u/info", "GET", {}, function (state, data) {
                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },

        login: function (phone, password, cb) {

            data = {
                "un": CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(phone)),
                "pw": String(CryptoJS.SHA1(password))
            }
            sendCmd("/wx/u/login", "POST", data, function (statue, data) {
                if (statue == 0) {
                    window.location.href = "/";
                } else {
                    alert(data.errorMeg);
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },

        register: function (regObject, cb) {
            obj = {
                ph:regObject.ph,
                password :regObject.password,
                confirmPassword:regObject.confirmPassword,
                confirmCode :regObject.confirmCode
            }

            obj.ph = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(regObject.ph));		// 将 WordArray 用 Base64 加密
            obj.password =  String(CryptoJS.SHA1(regObject.password))
            obj.confirmPassword = String(CryptoJS.SHA1(regObject.confirmPassword));

            sendCmd("/wx/u/reg", "POST", obj, function (statue, data) {
                if (statue == 0) {
                    alert("注册成功");
                    window.location.href = "/";
                } else {
                    alert("注册失败：" + data.errMsg);
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },
        getUserOrder: function (callback) {
            sendCmd('/wx/u/order', "GET", {}, function (state, data) {
                callback(state, data)
            })
        },

        recharge: function(rechargeNum,cb) {
            sendCmd("/wx/a/recharge", "POST", {rechargeNum: rechargeNum}, function (statue, data) {
                if (statue == 0) {
                    alert("充值成功，跳转到主页")
                    window.location.href = "/";
                } else {
                    alert("充值失败：" + data.errMsg);
                }
                if (cb != undefined) {
                    cb(state, data)
                }
            })
        }
    }
    return service
})
