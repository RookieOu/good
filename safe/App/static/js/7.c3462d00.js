(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[7],{"+mnW":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[t.searchable&&"top"===t.searchPlace?a("div",{staticClass:"search-con search-con-top"},[a("ButtonGroup",[t.outaddable?a("Button",{staticClass:"search-btn",attrs:{type:"primary"},on:{click:t.handleAdd}},[t._v("添加")]):t._e(),t._v(" "),t.outeditable?a("Button",{staticClass:"search-btn",on:{click:t.handleEdit}},[t._v("编辑")]):t._e(),t._v(" "),t.outviewable?a("Button",{staticClass:"search-btn",on:{click:t.handleView}},[t._v("查看")]):t._e(),t._v(" "),t.exportable?a("Button",{on:{click:t.exportExcel}},[t._v(t._s(t.exporttitle))]):t._e(),t._v(" "),t._t("extbuttons")],2),t._v(" "),a("div",{staticStyle:{float:"right"}},[a("Select",{staticClass:"search-col",style:t.searchkeystyle,model:{value:t.searchKey,callback:function(e){t.searchKey=e},expression:"searchKey"}},t._l(t.columns,function(e){return"handle"!==e.key&&""!==e.key&&"Array"!=e.type&&"Object"!=e.type&&"Boolean"!=e.type?a("Option",{key:"search-col-"+e.key,attrs:{value:e.key}},[t._v(t._s(e.title))]):t._e()})),t._v(" "),a("Input",{staticClass:"search-input",style:t.searchinputstyle,attrs:{clearable:"",placeholder:"输入关键字搜索"},on:{"on-change":t.handleClear,"on-keyup":function(e){return"button"in e||!t._k(e.keyCode,"enter",13,e.key,"Enter")?t.handleSearch(e):null}},model:{value:t.searchValue,callback:function(e){t.searchValue=e},expression:"searchValue"}}),t._v(" "),a("Button",{staticClass:"search-btn",attrs:{type:"primary"},on:{click:t.handleSearch}},[a("Icon",{attrs:{type:"search"}}),t._v("搜索")],1),t._v(" "),t.refreshable?a("Button",{staticClass:"search-btn",attrs:{type:"primary"},on:{click:t.handleRefresh}},[a("Icon",{attrs:{type:"md-refresh",size:"16"}})],1):t._e()],1)],1):t._e(),t._v(" "),a("Table",{ref:"tablesMain",attrs:{data:t.insideTableData,columns:t.insideColumns,stripe:t.stripe,border:t.border,"show-header":t.showHeader,width:t.width,height:t.height,loading:t.loading,"disabled-hover":t.disabledHover,"highlight-row":t.highlightRow,"row-class-name":t.rowClassName,size:t.size,"no-data-text":t.noDataText,"no-filtered-data-text":t.noFilteredDataText},on:{"on-current-change":t.onCurrentChange,"on-select":t.onSelect,"on-select-cancel":t.onSelectCancel,"on-select-all":t.onSelectAll,"on-selection-change":t.onSelectionChange,"on-sort-change":t.onSortChange,"on-filter-change":t.onFilterChange,"on-row-click":t.onRowClick,"on-row-dblclick":t.onRowDblclick,"on-expand":t.onExpand}},[t._t("header",null,{slot:"header"}),t._v(" "),t._t("footer",null,{slot:"footer"}),t._v(" "),t._t("loading",null,{slot:"loading"})],2),t._v(" "),a("div",{staticStyle:{margin:"10px",overflow:"hidden"}},[a("div",{staticStyle:{float:"right"}},[a("Page",{attrs:{total:t.data_show_total,current:t.data_show_page,"show-total":"","page-size":t.data_show_limit,"show-sizer":"","page-size-opts":[10,20,50,100]},on:{"on-change":t.handleChangeTablePage,"on-page-size-change":t.changePageSize}})],1)]),t._v(" "),t.searchable&&"bottom"===t.searchPlace?a("div",{staticClass:"search-con search-con-top"},[a("Select",{staticClass:"search-col",model:{value:t.searchKey,callback:function(e){t.searchKey=e},expression:"searchKey"}},t._l(t.columns,function(e){return"handle"!==e.key?a("Option",{key:"search-col-"+e.key,attrs:{value:e.key}},[t._v(t._s(e.title))]):t._e()})),t._v(" "),a("Input",{staticClass:"search-input",attrs:{placeholder:"输入关键字搜索"},model:{value:t.searchValue,callback:function(e){t.searchValue=e},expression:"searchValue"}}),t._v(" "),a("Button",{staticClass:"search-btn",attrs:{type:"primary"}},[a("Icon",{attrs:{type:"search"}}),t._v("  搜索")],1)],1):t._e(),t._v(" "),a("a",{staticStyle:{display:"none",width:"0px",height:"0px"},attrs:{id:"hrefToExportTable"}})],1)},i=[],l=(a("Vd3H"),a("91GP"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"tables-edit-outer"},[t.isEditting?a("div",{staticClass:"tables-editting-con"},[a("Input",{staticClass:"tables-edit-input",attrs:{value:t.value},on:{input:t.handleInput}}),t._v(" "),a("Button",{staticStyle:{padding:"6px 4px"},attrs:{type:"text"},on:{click:t.saveEdit}},[a("Icon",{attrs:{type:"md-checkmark"}})],1),t._v(" "),a("Button",{staticStyle:{padding:"6px 4px"},attrs:{type:"text"},on:{click:t.canceltEdit}},[a("Icon",{attrs:{type:"md-close"}})],1)],1):a("div",{staticClass:"tables-edit-con"},[a("span",{staticClass:"value-con"},[t._v(t._s(t.value))]),t._v(" "),t.editable?a("Button",{staticClass:"tables-edit-btn",staticStyle:{padding:"2px 4px"},attrs:{type:"text"},on:{click:t.startEdit}},[a("Icon",{attrs:{type:"md-create"}})],1):t._e()],1)])}),o=[],s={name:"TablesEdit",props:{value:[String,Number],edittingCellId:String,params:Object,editable:Boolean},computed:{isEditting:function(){return this.edittingCellId==="editting-".concat(this.params.index,"-").concat(this.params.column.key)}},methods:{handleInput:function(t){this.$emit("input",t)},startEdit:function(){this.$emit("on-start-edit",this.params)},saveEdit:function(){this.$emit("on-save-edit",this.params)},canceltEdit:function(){this.$emit("on-cancel-edit",this.params)}}},r=s,c=(a("Cgt2"),a("KHd+")),u=Object(c["a"])(r,l,o,!1,null,null,null),d=u.exports,h={delete:function(t,e,a){return t("Poptip",{props:{confirm:!0,title:"你确定要删除吗?"},on:{"on-ok":function(){a.$emit("on-delete",e),a.$emit("input",e.tableData.filter(function(t,a){return a!==e.row.initRowIndex}))}}},[t("Button",{props:{type:"text",ghost:!0}},[t("Icon",{props:{type:"md-trash",size:18,color:"#000000"}})])])}},f=h,p=a("wnYN"),b=(a("MNn9"),{name:"Tables",props:{value:{type:Array,default:function(){return[]}},columns:{type:Array,default:function(){return[]}},size:String,width:{type:[Number,String]},height:{type:[Number,String]},stripe:{type:Boolean,default:!1},border:{type:Boolean,default:!1},showHeader:{type:Boolean,default:!0},highlightRow:{type:Boolean,default:!1},rowClassName:{type:Function,default:function(){return""}},context:{type:Object},noDataText:{type:String},noFilteredDataText:{type:String},disabledHover:{type:Boolean},loading:{type:Boolean,default:!1},editable:{type:Boolean,default:!1},searchable:{type:Boolean,default:!1},exporttitle:{type:String,default:"导出为Csv文件"},searchinputstyle:{type:Object,default:function(){return{}}},searchkeystyle:{type:Object,default:function(){return{}}},searchPlace:{type:String,default:"top"},outeditable:{type:Boolean,default:!1},outviewable:{type:Boolean,default:!0},exportable:{type:Boolean,default:!0},outaddable:{type:Boolean,default:!0},refreshable:{type:Boolean,default:!1}},data:function(){return{insideColumns:[],insideTableData:[],initTableData:[],initTableValue:[],initFilterData:[],initSortData:[],edittingCellId:"",edittingText:"",searchValue:"",searchKey:"",data_show_total:0,data_show_page:1,data_show_limit:10,order:"",orderkey:"",ordertype:""}},methods:{suportEdit:function(t,e){var a=this;return t.render=function(t,e){return t(d,{props:{params:e,value:a.insideTableData[e.index][e.column.key],edittingCellId:a.edittingCellId,editable:a.editable},on:{input:function(t){a.edittingText=t},"on-start-edit":function(t){a.edittingCellId="editting-".concat(t.index,"-").concat(t.column.key),a.$emit("on-start-edit",t)},"on-cancel-edit":function(t){a.edittingCellId="",a.$emit("on-cancel-edit",t)},"on-save-edit":function(t){a.value[t.row.initRowIndex][t.column.key]=a.edittingText,a.$emit("input",a.value),a.$emit("on-save-edit",Object.assign(t,{value:a.edittingText})),a.edittingCellId=""}}})},t},surportHandle:function(t){var e=this,a=t.options||[],n=[];a.forEach(function(t){f[t]&&n.push(f[t])});var i=t.button?[].concat(n,t.button):n;return t.render=function(t,a){return a.tableData=e.value,t("div",i.map(function(n){return n(t,a,e)}))},t},handleColumns:function(t){var e=this;this.insideColumns=t.map(function(t,a){var n=t;return n.editable&&(n=e.suportEdit(n,a)),"handle"===n.key&&(n=e.surportHandle(n)),n})},setDefaultSearchKey:function(){void 0!=this.columns[0]&&(this.searchKey="handle"!==this.columns[0].key?this.columns[0].key:this.columns.length>1?this.columns[1].key:"")},handleClear:function(t){""===t.target.value&&this.handleSearch()},handleSearch:function(){var t=this;this.initFilterData=this.initTableValue.filter(function(e){var a=Object(p["o"])(e[t.searchKey]),n="";return n="object"==a||"array"==a?JSON.stringify(e[t.searchKey]):e[t.searchKey].toString(),n.toLowerCase().indexOf(t.searchValue.toLowerCase())>-1}),this.handleSort()},handleTableData:function(){this.initTableValue=this.value.map(function(t,e){var a=t;return a&&(a.initRowIndex=e),a}),this.handleSearch()},handleSort:function(){this.initSortData=this.initFilterData,this.initSortData.sort(this.compare(this.orderkey,this.ordertype,this.order)),this.handlePage()},handlePage:function(){this.data_show_total=this.initSortData.length,this.insideTableData=this.initSortData.slice((this.data_show_page-1)*this.data_show_limit,(this.data_show_page-1)*this.data_show_limit+this.data_show_limit)},compare:function(t,e,a){return function(n,i){var l=n[t],o=i[t];return"Number"===e?"asc"===a?l-o:o-l:"Date"===e?"asc"===a?new Date(l)-new Date(o):new Date(o)-new Date(l):"asc"===a?l>o:o>l}},handleChangeTablePage:function(t){this.data_show_page=t,this.handlePage()},changePageSize:function(t){this.data_show_limit=t,this.handlePage()},exportCsv:function(t){this.$refs.tablesMain.exportCsv(t)},clearCurrentRow:function(){this.$refs.talbesMain.clearCurrentRow()},onCurrentChange:function(t,e){this.$emit("on-current-change",t,e)},onSelect:function(t,e){this.$emit("on-select",t,e)},handleEdit:function(){this.$emit("on-edit")},handleView:function(){this.$emit("on-view")},handleRefresh:function(){this.$emit("on-refresh")},onSelectCancel:function(t,e){this.$emit("on-select-cancel",t,e)},onSelectAll:function(t){this.$emit("on-select-all",t)},onSelectionChange:function(t){this.$emit("on-selection-change",t)},onSortChange:function(t,e,a){this.order=t.order,this.orderkey=t.key,this.ordertype=t.column.type?t.column.type:"",this.handleSort()},onFilterChange:function(t){this.$emit("on-filter-change",t)},onRowClick:function(t,e){this.$emit("on-row-click",t,e)},onRowDblclick:function(t,e){this.$emit("on-row-dblclick",t,e)},onExpand:function(t,e){this.$emit("on-expand",t,e)},exportExcel:function(){this.$refs.tablesMain.exportCsv({filename:"table-".concat((new Date).valueOf(),".csv")})},handleAdd:function(){this.$emit("on-add")}},watch:{columns:function(t){this.handleColumns(t),this.setDefaultSearchKey()},value:function(t){this.handleTableData()}},mounted:function(){this.handleColumns(this.columns),this.setDefaultSearchKey(),this.handleTableData()}}),m=b,v=Object(c["a"])(m,n,i,!1,null,null,null),y=v.exports;e["a"]=y},"/DHG":function(t,e,a){"use strict";var n=a("liDa"),i=a.n(n);i.a},"3jbP":function(t,e,a){},"5cRF":function(t,e,a){"use strict";var n=a("SfSJ"),i=a.n(n);i.a},"94sW":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("Card",[a("tables",{ref:"tables",attrs:{outeditable:"",searchable:"","highlight-row":"","search-place":"top",columns:t.columns},on:{"on-delete":t.handleDelete,"on-current-change":t.handleSelect,"on-edit":t.handleEdit,"on-add":t.handleAdd,"on-view":t.handleView},model:{value:t.tableData,callback:function(e){t.tableData=e},expression:"tableData"}})],1),t._v(" "),a("privatemodel",{attrs:{title:t.modaltitle,edittype:t.modeledittype}})],1)},i=[],l=a("yT7P"),o=a("+mnW"),s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("public-modal",{attrs:{title:t.title,nofooter:"0"==t.edittype,width:"800"},on:{"on-ok":function(e){t.handleCommit("formValidate")},"on-cancel":function(e){t.handleReset("formValidate")}},model:{value:t.showModal,callback:function(e){t.showModal=e},expression:"showModal"}},[a("Form",{ref:"formValidate",attrs:{model:t.model,rules:t.rule,"label-width":80}},[a("FormItem",{attrs:{label:"名称",prop:"name"}},[a("Input",{attrs:{placeholder:"请输入名称"},model:{value:t.model.name,callback:function(e){t.$set(t.model,"name",e)},expression:"model.name"}})],1),t._v(" "),a("FormItem",{attrs:{label:"权限"}},[a("cascaderMulti",{attrs:{data:t.casdata,multiple:"",placeholder:"权限",trigger:"hover"},model:{value:t.model.privs,callback:function(e){t.$set(t.model,"privs",e)},expression:"model.privs"}})],1),t._v(" "),a("FormItem",{attrs:{label:"说明"}},[a("Input",{attrs:{placeholder:"请输入说明...",type:"textarea",rows:2},model:{value:t.model.desc,callback:function(e){t.$set(t.model,"desc",e)},expression:"model.desc"}})],1)],1)],1)],1)},r=[],c=(a("f3/d"),a("L2JU")),u=a("ULSL"),d=a("yk3/"),h=a("wnYN"),f={name:"Privatemodel",components:{publicModal:u["a"]},props:{title:{type:String,default:function(){return""}},edittype:{type:String,default:function(){return"0"}}},data:function(){return{initModel:{name:"",privs:[],desc:""},model:{name:"",privs:[],desc:""},typeList:[],rule:{name:[{required:!0,message:"名称不能为空",trigger:"blur"}],storeid:[{required:!0,message:"商家不能为空",trigger:"blur"}]},casdata:[]}},watch:{"$store.state.burole.burole_edit_obj":function(t){this.model=Object(h["c"])(this.$store.state.burole.burole_edit_obj)}},computed:{showModal:{get:function(){return this.$store.state.burole.burole_edit_show},set:function(t){this.$store.state.burole.burole_edit_show=t}}},methods:Object(l["a"])({},Object(c["b"])(["handleCreateBurole","handleUpdateBurole"]),{init:function(){"1"===this.edittype?this.model=Object(h["c"])(this.initModel):"2"===this.edittype&&(this.$store.state.burole.burole_edit_obj=Object(h["c"])(this.$store.state.burole.burole_select_obj))},handleReset:function(t){this.$refs[t].resetFields(),this.init()},handleCommit:function(t){var e=this;this.$refs[t].validate(function(a){a?"1"===e.edittype?e.$store.dispatch("handleCreateBurole",{form:e.model}).then(function(a){e.$refs[t].resetFields(),e.init(),e.$Message.success("Success!")}).catch(function(t){e.$Message.error(t)}):"2"===e.edittype&&e.$store.dispatch("handleUpdateBurole",{form:e.model}).then(function(a){e.$refs[t].resetFields(),e.init(),e.$Message.success("Success!")}).catch(function(t){e.$Message.error(t)}):e.$Message.error("Fail!")})}}),mounted:function(){var t=this;Object(d["a"])("get").then(function(e){var a=e.data.data;t.treeData=a.filter(function(t){return"数据权限"==t.name})[0];for(var n=0;n<t.treeData.value.length;n++)t.casdata.push(Object(h["n"])(t.treeData.value[n]))})},created:function(){this.model=Object(h["c"])(this.initModel)}},p=f,b=(a("ZpkK"),a("KHd+")),m=Object(b["a"])(p,s,r,!1,null,null,null),v=m.exports,y={name:"Burole",components:{Tables:o["a"],Privatemodel:v},data:function(){return{modaltitle:"",modeledittype:"0",selectData:{},columns:[{title:"名称",key:"name",type:"String",sortable:!0,editable:!0},{title:"说明",key:"desc",type:"String",editable:!0},{title:"操作",key:"handle",button:[function(t,e,a){return t("Poptip",{props:{confirm:!0,title:"你确定要删除吗?"},on:{"on-ok":function(){a.$emit("on-delete",e)}}},[t("Button","删除")])}]}],addModal:{name:"",privs:[],desc:""}}},methods:Object(l["a"])({},Object(c["b"])(["handleGetBurole","handleDeleteBurole"]),{handleDelete:function(t){var e=this;t.row.id?this.$store.dispatch("handleDeleteBurole",t.row.id).then(function(t){e.selectData=JSON.parse(JSON.stringify({})),e.$Message.success("Success!")}).catch(function(t){e.$Message.error(t)}):this.$Message.error("请先选择数据")},handleAdd:function(){this.modaltitle="添加",this.modeledittype="1",this.$store.state.burole.burole_edit_obj=Object(h["c"])(this.addModal),this.$store.state.burole.burole_edit_show=!0},handleEdit:function(){this.selectData.id?(this.modaltitle="编辑",this.modeledittype="2",this.$store.state.burole.burole_edit_obj=Object(h["c"])(this.selectData),this.$store.state.burole.burole_select_obj=Object(h["c"])(this.selectData),this.$store.state.burole.burole_edit_show=!0):this.$Message.error("请先选择数据")},handleView:function(){this.selectData.id?(this.modaltitle="查看",this.modeledittype="0",this.$store.state.burole.burole_edit_obj=Object(h["c"])(this.selectData),this.$store.state.burole.burole_select_obj=Object(h["c"])(this.selectData),this.$store.state.burole.burole_edit_show=!0):this.$Message.error("请先选择数据")},handleSelect:function(t,e){this.selectData=JSON.parse(JSON.stringify(t))}}),computed:{tableData:{get:function(){return this.$store.state.burole.burole_list}}},mounted:function(){0===this.tableData.length&&this.$store.dispatch("handleGetBurole").then(function(t){})}},_=y,g=(a("/DHG"),Object(b["a"])(_,n,i,!1,null,null,null)),w=g.exports;e["default"]=w},Cgt2:function(t,e,a){"use strict";var n=a("3jbP"),i=a.n(n);i.a},LyE8:function(t,e,a){"use strict";var n=a("eeVq");t.exports=function(t,e){return!!t&&n(function(){e?t.call(null,function(){},1):t.call(null)})}},MNn9:function(t,e,a){},"Q+Nu":function(t,e,a){},SfSJ:function(t,e,a){},ULSL:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticStyle:{position:"relative"}},[a("Modal",{ref:"public_modal",class:"publicModal public-modal-layer"+t.layer,attrs:{width:t.fullscreen||t.fullscreen_status_value?null:t.width,styles:t.fullscreen||t.fullscreen_status_value?null:{top:t.top},fullscreen:t.fullscreen||t.fullscreen_status_value,loading:t.loading,closable:t.closable,"mask-closable":t.maskClosable,title:t.title,"ok-text":t.oktext,"cancel-text":t.canceltext,"footer-hide":t.nofooter,transfer:t.transfer},on:{"on-ok":t.buttonOk,"on-cancel":t.buttonCancel,"on-visible-change":t.visibleChange},model:{value:t._visible,callback:function(e){t._visible=e},expression:"_visible"}},[a("div",{staticClass:"ivu-modal-header-inner no-select",staticStyle:{"padding-right":"20px",position:"relative",overflow:"visible"},attrs:{slot:"header"},slot:"header"},[a("Icon",{attrs:{type:t.icon}}),t._v("\r\n        "+t._s(t.title)+"\r\n        "),a("div",{staticClass:"custom-icon"},[t._t("extra-icon"),t._v(" "),a("Tooltip",{attrs:{slot:"extra-icon",content:"重置表单"},slot:"extra-icon"},[t.clearable?a("Icon",{attrs:{size:14,custom:"cmdb-font font-clearup"},nativeOn:{click:function(e){return t.buttonClear(e)}}}):t._e()],1),t._v(" "),a("Tooltip",{attrs:{slot:"extra-icon",content:t.fullscreen_status_value?"取消全屏":"全屏"},slot:"extra-icon"},[t.fullscreen?t._e():a("Icon",{attrs:{size:16,type:t.fullscreen_status_value?"md-contract":"md-expand"},nativeOn:{click:function(e){t.fullscreen_status_value=!t.fullscreen_status_value}}})],1)],2),t._v(" "),a("div",{staticClass:"custom-btn"},[t._t("extra-button")],2)],1),t._v(" "),a("div",{staticClass:"ivu-card-body",staticStyle:{position:"relative"},style:void 0!==t.bodyPadding?"padding:0!important;":""+!t.fullscreen_status_value&&t.scrollable?{height:t.cmdb.main_scrollheight+55+"px","overflow-y":"auto"}:""},[t._t("default")],2),t._v(" "),t._t("footer",null,{slot:"footer"})],2)],1)},i=[],l=a("yT7P"),o=a("L2JU"),s={name:"",data:function(){return{fullscreen_status_value:this.fullscreen_status}},computed:Object(l["a"])({},Object(o["d"])(["cmdb"]),{_visible:{get:function(){return this.value},set:function(t){this.$emit("input",t)}}}),watch:{fullscreen_status_value:function(t){this.$emit("full-change",t)}},props:{value:{type:Boolean,default:!1},loading:{type:Boolean,default:!1},closable:{type:Boolean,default:!0},transfer:{type:Boolean,default:!0},maskClosable:{type:Boolean,default:!0},clearable:{type:Boolean,default:!1},nofooter:{type:Boolean,default:!1},fullscreen:{type:Boolean,default:!1},scrollable:{type:Boolean,default:!1},fullscreen_status:{type:Boolean,default:!1},width:{type:String,default:"50%"},top:{type:String,default:"20px"},title:{type:String,default:""},oktext:{type:String,default:"确定"},canceltext:{type:String,default:"取消"},icon:{type:String,default:""},layer:{type:Number,default:0},bodyPadding:{type:Number,default:function(){}}},methods:{buttonOk:function(){this.$emit("on-ok",this)},buttonCancel:function(){var t=this;this.$emit("on-cancel",this),setTimeout(function(){t.fullscreen_status_value=t.fullscreen_status},300)},buttonClear:function(){this.$emit("on-clear",this)},visibleChange:function(t){this.$emit("on-visible-change",this)}},created:function(){},mounted:function(){}},r=s,c=(a("5cRF"),a("KHd+")),u=Object(c["a"])(r,n,i,!1,null,null,null);e["a"]=u.exports},Vd3H:function(t,e,a){"use strict";var n=a("XKFU"),i=a("2OiF"),l=a("S/j/"),o=a("eeVq"),s=[].sort,r=[1,2,3];n(n.P+n.F*(o(function(){r.sort(void 0)})||!o(function(){r.sort(null)})||!a("LyE8")(s)),"Array",{sort:function(t){return void 0===t?s.call(l(this)):s.call(l(this),i(t))}})},ZpkK:function(t,e,a){"use strict";var n=a("Q+Nu"),i=a.n(n);i.a},liDa:function(t,e,a){},"yk3/":function(t,e,a){"use strict";a.d(e,"a",function(){return l}),a.d(e,"b",function(){return o});var n=a("Zt8a"),i=n["a"].axios,l=function(t){return i.request({url:"get_privs_data",method:"get",params:{action:t}})},o=function(t){var e=t.form,a={form:e};return i.request({url:"get_privs_data",method:"put",data:a})}}}]);