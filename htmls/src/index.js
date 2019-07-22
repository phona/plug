'use strict';

// const webpack = require('webpack');
// const htmlwebpackplugin = require('html-webpack-plugin')

module.exports = {
	mode: 'development',
	entry: [
		'./src/main.js'
	],
	module: {
		rules: [
			{
				test: /\.vue$/,
				loader: 'vue-loader',
			}
		]
	},
}