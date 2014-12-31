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
	.controller('workStatementController', ['$scope', function($scope){
		$scope.dialogs = {
			title: 'Statement of Earnings and Deductions',
			sub_title_one: 'Input Earnings and Deductions'
		}
	}])