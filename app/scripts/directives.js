'use strict';

angular.module('bankApp.directives', [
	'bankApp.controllers'
	])
	.directive('menubar', function(){
		return{
			restrict: 'E',
			templateUrl: 'templates/menubar.html'
		}
	})