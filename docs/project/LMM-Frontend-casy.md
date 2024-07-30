---
title: LMM-Frontend-casy
order: 3
toc: content
nav:
 title: 项目记录
 order: 6
group:
 title: 项目记录
 order: 3
---
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
