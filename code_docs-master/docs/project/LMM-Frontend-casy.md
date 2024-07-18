<!--
 * @Author: sheng.zeng 1218128305@qq.com
 * @Date: 2024-07-16 11:36:31
 * @LastEditors: sheng.zeng 1218128305@qq.com
 * @LastEditTime: 2024-07-18 18:51:21
 * @FilePath: \LMM-Frontend\project.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
## 项目路径
D:\w\lmm\LMM-Frontend

## aggrid 数据更新之后的回调 `@row-data-updated`

``` vue
 <AgGridVue style="width: 100%; height: 70vh;" @row-data-updated="onRowDataUpdated" />
```

``` js
const onRowDataUpdated = (event) => {
    console.log(event)
    // 默认选中复选框
    const nodesToSelect = [];
    for (let item of selectedRow.value) {
        gridApi.value.forEachNode((node) => {
            if (node.data.id === item.id) {
                console.log(node)
                // nodesToSelect.push(node);
                node.setSelected(true);
            }
        });
    }
    console.log(nodesToSelect)
    // 这样也可以 默认选中复选框
    // if (nodesToSelect.length > 0) {
    //     gridApi.value.setNodesSelected({ nodes: nodesToSelect, newValue: true });
    // }
}
```
