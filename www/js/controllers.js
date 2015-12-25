angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope, PollingFactory) {


  $scope.cards = [
    {'month': 'JUN', 'day': '29', 'city': 'Chiang Mai', 'temp': '69'},
    {'month': 'OCT', 'day': '22', 'city': 'River Styx', 'temp': '32'},
    {'month': 'NOV', 'day': '01', 'city': 'Bahstin', 'temp': '15'}
  ];

   $scope.currency_data = {};

   $scope.pollThailand = function () {

    PollingFactory.pollOnce('/currency/THB', function (api_data){
      $scope.currency_data = api_data;
      console.log($scope.currency_data);
    })

  };

  $scope.pollThailand();
})

.controller('ChatsCtrl', function($scope, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  $scope.currency_data = {}

  $scope.settings = {
    enableFriends: true
  };

});
