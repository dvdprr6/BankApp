'use strict';

angular.module('bankApp.controllers',[
	'bankApp.directives'
	])
	.controller('menubarController', ['$scope', function($scope){
		$scope.tabs = {
			name: 'Bank Webapp',
			work_statement: 'Work Statement'
		};
	}])