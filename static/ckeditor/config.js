/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	// 工具栏配置
	config.toolbarGroups = [
		{ name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing', groups: [ 'find', 'selection', 'spellchecker', 'editing' ] },
		{ name: 'forms', groups: [ 'forms' ] },
		'/',
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
		{ name: 'links', groups: [ 'links' ] },
		{ name: 'insert', groups: [ 'insert' ] },
		'/',
		{ name: 'styles', groups: [ 'styles' ] },
		{ name: 'colors', groups: [ 'colors' ] },
		{ name: 'tools', groups: [ 'tools' ] },
		{ name: 'others', groups: [ 'others' ] },
		{ name: 'about', groups: [ 'about' ] }
	];
	// 去掉图片预览框的文字
	config.image_previewText = ' ';
	// 隐藏“超链接”与“高级选项”只留上传和预览按钮
	config.removeDialogTabs = 'image:advanced;image:Link;','help';
	// 开启工具栏“图像”中文件上传功能，后面的url为图片上传要指向的的action或servlet
	config.filebrowserImageUploadUrl= "/blog/uploadFile/";

	//当用户键入TAB时，编辑器走过的空格数，当值为0时，焦点将移出编辑框 plugins/tab/plugin.js
	config.tabSpaces = 4;
	//从word中粘贴内容时是否移除格式
	config.pasteFromWordRemoveStyle = false;
	//设置快捷键
	config.keystrokes = [
		[CKEDITOR.CTRL + 13 /*Enter*/, "maximize"],
		[CKEDITOR.ALT + 121 /*F10*/, "toolbarFocus"], //获取焦点
		[CKEDITOR.ALT + 122 /*F11*/, "elementsPathFocus"], //元素焦点
		[CKEDITOR.SHIFT + 121 /*F10*/, "contextMenu"], //文本菜单
		[CKEDITOR.CTRL + 90 /*Z*/, "undo"], //撤销
		[CKEDITOR.CTRL + 89 /*Y*/, "redo"], //重做
		[CKEDITOR.CTRL + CKEDITOR.SHIFT + 90 /*Z*/, "redo"], //
		[CKEDITOR.CTRL + 76 /*L*/, "link"], //链接
		[CKEDITOR.CTRL + 66 /*B*/, "bold"], //粗体
		[CKEDITOR.CTRL + 73 /*I*/, "italic"], //斜体
		[CKEDITOR.CTRL + 85 /*U*/, "underline"], //下划线
		[CKEDITOR.ALT + 109 /*-*/, "toolbarCollapse"],
	];
	//设置字体
	config.font_names = "黑体/黑体;楷体/楷体_GB2312;隶书/隶书;幼圆/幼圆;微软雅黑/微软雅黑;" + config.font_names;
	 
};
