routeapp.controller('welcome_page_ctrl', function($scope, Project_Group) {
    $scope.project_id = (window.location.pathname).split('/')[3];
    console.log($scope.project_id);
    if($scope.project_id != ''){
        Project_Group.get({id:$scope.project_id},function(item){
        $scope.project_group = item;
        console.log(item);
        });
    };
    $scope.myInterval = 5000;
  var slides = $scope.slides = [];
  $scope.addSlide = function() {
    var newWidth = 600 + slides.length + 1;
    slides.push({
      image: 'http://placekitten.com/' + newWidth + '/300',
      text: ['鼠标停留在图片','查询分支可搜','拉取版本不填写版本，则拉去当前版本','执行时请不要离开或点击左侧'][slides.length % 4] +
        ['上查看项目说明', '索到所有版本', '，选择所要拉的项目，批量拉取即可', '标签，否则将看不到日志'][slides.length % 4]
    });
  };
  for (var i=0; i<4; i++) {
    $scope.addSlide();
  }
});
