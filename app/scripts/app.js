'use strict';

angular.module('bankApp', [
	'bankApp.controllers',
	'bankApp.directives',
	'ngRoute'
	])
	.config(['$routeProvider', function($routeProvider){
		$routeProvider.when('/work_statement', {
			templateUrl: 'templates/work_statement.html',
			controller: 'workStatementController'
		});
	}]);