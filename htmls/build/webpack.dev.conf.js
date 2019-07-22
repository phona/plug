'use strict';

const path = require('path');
const webpack = require('webpack');
const { VueLoaderPlugin } = require('vue-loader');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
	devServer: {
		contentBase: path.join(__dirname, 'dist'),
		compress: true,
		host: 'localhost',
		port: 9000,
		proxy: {
			'/apis': {
				target: 'http://localhost:5000',
				secure: false
			},
		},
	},

	entry: [
		'./src/main.js'
	],

	resolve: {
		extensions: ['.js', '.vue', '.json'],
		alias: {
			'vue$': 'vue/dist/vue.esm.js',
			'@': '../src',
			'static': path.resolve(__dirname, '../static'),
		}
	},

	module: {
		rules: [
			{
				test: /\.vue$/,
				use: 'vue-loader'
			},

			{
				test: /\.css$/,
				use: [
				  'vue-style-loader',
				  'css-loader'
				]
			},

			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [
					'file-loader'
				]
			},

			{
				test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
				use: 'url-loader',
			}
		]
	},

	plugins: [
		new webpack.HotModuleReplacementPlugin(),
		new VueLoaderPlugin(),
		new HtmlWebpackPlugin({
			template: './public/index.html',
			filename: 'index.html',
			inject: true
		})
	]
};