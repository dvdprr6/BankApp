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
		$scope.valueReturn = {
			data:{
				companies:['Longbow Advantage','Nuance Communications Inc.'],
				years:['2011','2012', '2014']
			}
		}
		$scope.companyList = $scope.valueReturn.data.companies
		console.log($scope.companyList)
		$scope.company = $scope.companyList[0]
		$scope.yearList = $scope.valueReturn.data.years
		$scope.year = $scope.yearList[0]
	}])