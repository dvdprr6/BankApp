'use strict';

var LIVERELOAD_PORT = 35729;

module.exports = function(grunt){

	require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		
		yeoman:{
			app: require('./bower.json').appPath || 'app'
		},

		connect:{
			client:{
				options:{
					hostname:'0.0.0.0',
					port: 9000,
					base: '<%= yeoman.app %>',
					livereload: LIVERELOAD_PORT
				}
			}
		},

		watch:{
			client:{
				files: ['app/**/*'],
				tasks:[],
				options:{
					livereload:LIVERELOAD_PORT
				}
			}
		}
	});

	grunt.registerTask('server', ['connect:client','watch:client']);
};