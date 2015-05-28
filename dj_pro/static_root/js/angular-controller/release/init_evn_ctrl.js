routeapp.controller('init_env_control', function($scope, $http){

    selected_items = [];

    function common(bro, url, ctype, i){
        $scope.pull_show = 'disabled';
        $scope.wait_msg = '请稍作等待，不要切换页面，否则无法看到日志';
        $scope.wait_flag = true;
        i = typeof i !== 'undefined' ? i : 0;
        console.log(bro);
        console.log(i)
        if(ctype == 'multi'){
            pro = bro[i];
            console.log(pro);
            i += 1;
        }else{
            pro = bro;
        };
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
            console.log(result);
            console.log(1+$scope.error_log+1);
            if(ctype == 'mulit'){
                common_insert(pro, url, ctype, i);
            };
        }).error(function(err){
            alert('error');
            $scope.pull_show = '';
            $scope.wait_flag = false;
            $scope.wait_msg = '';
        });
    };
    

    function common_insert(item, url, ctype, i){
        
        common(item, url, ctype, i);
    };

    function common_post(pro, url){
        $http({
            method: 'POST',
            url: url,
            data: pro
        }).success(function(result){
            $scope.yml_set = result;
            console.log(result);
        }).error(function(err){
            console.log('error');
        });
    };

    $scope.checkAll = function () {                               
        if ($scope.selectedAll) {                                 
            $scope.selectedAll = false;                           
        } else {                                                  
            $scope.selectedAll = true;                            
        }                                                         
        angular.forEach($scope.yml_set, function (item) { 
            item.Selected = $scope.selectedAll;                   
        });                                                       
                                                              
    };

    $scope.find_items = function(pro){
        $scope.pro = {};
        $scope.pro.init_book = '/data/ansible/lnmp/roles/tasks.txt';
        $scope.pro.separate_book = '/data/ansible/lnmp/roles/separate.yml';
        $scope.pro.pro_group = 'lnmp';
        common_post($scope.pro,'/release/project_item_api/init_env_items/');
    };

    $scope.excute_single = function(vars){
        $scope.pro.myhost = '192.168.1.54';
        console.log(vars);
        $scope.pro.process_vars = vars.item;
        $scope.pro.pro_name = vars.item;
        common($scope.pro, '/release/project_item_api/single_env_install/');
    };

    $scope.excute_selected = function(){
        $(".selected input:checked").each ( function() {
            $scope.pro.myhost = '192.168.1.54';
            $scope.pro.process_vars = $(this).val();
            $scope.pro.pro_name = $(this).val();
            selected_items.push($scope.pro);
        });
        console.log(selected_items);
        common(selected_items, '/release/project_item_api/single_env_install/', 'multi');
    }

        $scope.progress = 0;
        for(i = 0; i <=99; i++){
            $scope.progress += 1;
            console.log($scope.progress);
        };

    });

