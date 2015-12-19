angular.module('starter.services', [])

.factory('Chats', function() {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var chats = [{
    id: 0,
    name: 'Ben Sparrow',
    lastText: 'You on your way?',
    face: 'img/ben.png'
  }, {
    id: 1,
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'img/max.png'
  }, {
    id: 2,
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'img/adam.jpg'
  }, {
    id: 3,
    name: 'Perry Governor',
    lastText: 'Look at my mukluks!',
    face: 'img/perry.png'
  }, {
    id: 4,
    name: 'Mike Harrington',
    lastText: 'This is wicked good ice cream.',
    face: 'img/mike.png'
  }];

  return {
    all: function() {
      return chats;
    },
    remove: function(chat) {
      chats.splice(chats.indexOf(chat), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < chats.length; i++) {
        if (chats[i].id === parseInt(chatId)) {
          return chats[i];
        }
      }
      return null;
    }
  };
})

.factory('PollingFactory',['$http','$interval', function($http, $interval){
       //TODO Figure out how to best handle yet-to-be-added polls i.e. quick route changes
       // var baseUrl = "http://10.246.226.151:8000";
        var baseUrl = "http://127.0.0.1:5000";
        //var defaultPollingTime = 10000;
        var polls = {};

        //function listPolls(){
        //    //console.log("ALL POLLS: ".concat(Object.keys(polls).length));
        //    for(var key in polls){
        //        ////console.log(key.concat(": ").concat(polls[key]));
        //    }
        //}

        function pollOnce(path, callback) {
            url = baseUrl.concat(path);
            $http.get(url)
                .success(callback);
        }

        //function startPolling(name, path, pollingTime, callback) {
        //    // Check to make sure poller doesn't already exist
        //    if (!polls[name]) {
        //        polls[name] = $interval(function(){pollOnce(path, callback)}, pollingTime || defaultPollingTime);
        //        ////console.log("STARTING ".concat(pollingTime/1000).concat(" second polling for: ").concat(path));
        //    }
        //}
        //
        //function stopPolling(name) {
        //    if(polls[name]){
        //        $interval.cancel(polls[name]);
        //        delete polls[name];
        //        ////console.log("STOPPING polling on ".concat(name));
        //    }
        //    else{
        //        ////console.log("INFO: No polling found for ".concat(name));
        //    }
        //}

        return{
            pollOnce: pollOnce
            //startPolling: startPolling,
            //stopPolling: stopPolling,
            //listPolls: listPolls
        }
}]);

