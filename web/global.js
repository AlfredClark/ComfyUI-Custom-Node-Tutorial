// 全局通用Web脚本
// 引用app脚本
import {app} from "../../scripts/app.js";

// 注册拓展脚本
app.registerExtension({
    // 拓展名称，注意要保持唯一性
    name: "GlobalExtension",
    // 当 Comfy 网页被加载（或重新加载）时调用，调用时机是在图对象已创建，但还未注册或创建任何节点之前
    async init() {
        console.log("Global Hooks: init()")
    },
    // 在启动流程结束时调用。适合添加事件监听器（无论是 Comfy 事件还是 DOM 事件），或添加全局菜单
    async setup() {
        console.log("Global Hooks: setup()");
    },
    // 对每种节点类型调用一次，用于修改节点的行为
    async beforeRegisterNodeDef() {
        console.log("Global Hooks: beforeRegisterNodeDef()");
    },
    // 当某个节点实例被创建时调用，在这个钩子里你可以修改节点的具体实例。
    async nodeCreated() {
        console.log("Global Hooks: nodeCreated()");
    },
    // 添加自定义节点时调用
    async addCustomNodeDefs() {
        console.log("Global Hooks: addCustomNodeDefs()");
    },
    // 获得自定义组件时调用
    async getCustomWidgets() {
        console.log("Global Hooks: getCustomWidgets()");
    },
    // 注册自定义节点时调用
    async registerCustomNodes() {
        console.log("Global Hooks: registerCustomNodes()");
    },
    // 加载工作流之前调用
    async beforeConfigureGraph() {
        console.log("Global Hooks: beforeConfigureGraph()");
    },
    // 加载工作流之后调用
    async afterConfigureGraph() {
        console.log("Global Hooks: afterConfigureGraph()");
    },
    // 加载工作流节点
    loadedGraphNode() {
        console.log("Global Hooks: loadedGraphNode()");
    },
})
