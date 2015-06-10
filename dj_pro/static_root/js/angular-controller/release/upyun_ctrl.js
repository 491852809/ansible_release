routeapp.controller('upyun_control', function($scope, $http){

    function common(bro, url, ctype, i, num){
        $scope.pull_show = 'disabled';
        $scope.wait_msg = '请稍作等待，不要切换页面，否则无法看到日志';
        $scope.wait_flag = true;
        i = typeof i !== 'undefined' ? i : 0;
        console.log(bro);
        console.log(i)
        $http({
            method: 'POST',
            url: url,
            data: JSON.stringify(pro),
        }).success(function(result){
            $scope.simple_log += result[0];
            $scope.complex_log += result[1]
            $scope.pull_show = '';
            $scope.wait_msg = '';
            $scope.wait_flag = false;
            $scope.cost_time = [];
            $scope.cost_time[pro.pro_name] = result[2];
            console.log(pro.pro_name + $scope.cost_time[pro.pro_name]);
            $scope.error_log += result[3];
            $scope.all_cost_time = result[2];
            console.log(1+$scope.error_log+1);
            $scope.progress = progress_num;
        }).error(function(err){
            alert('error');
            $scope.pull_show = '';
            $scope.wait_flag = false;
            $scope.wait_msg = '';
        });
    };
    


    function common_post(pro, url, type){
        $http({
            method: 'POST',
            url: url,
            data: pro
        }).success(function(result){
            if(type == 'upinfo'){
                $scope.up_info = result;
            };
            console.log(result);
        }).error(function(err){
            console.log('error');
        });
    };
    
    up_set = {};
    $scope.data_get = function(dir){
        up_set.space = $scope.up_sp;
        up_set.username = $scope.up_un;
        up_set.password = $scope.up_pw;
        up_set.dir = dir;
        console.log(up_set);
        common_post(up_set, '/release/project_var_api/upyun_get_info/', 'upinfo');
    };

});

