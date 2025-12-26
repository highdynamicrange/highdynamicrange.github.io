# 前后端项目创建
基于vue3和？

## backend part

```java
@CrossOrigin
@RestController
@RequestMapping("pk/")
public class BotInfoController {

    @RequestMapping("getbotinfo/")
    public Map<String, String> getBotInfo(){
        Map<String, String> bot1 = new HashMap<>();
        bot1.put("name", "tiger");
        bot1.put("rating", "1500");
        return bot1;
    }
}
```

重点在于三个注解：
- `@CrossOrigin`：核心解决跨域，可在类 / 方法级配置，生产环境需限制允许的源，避免全开放；
- `@RestController`：RESTful 接口必备，替代 `@Controller` + `@ResponseBody`，直接返回数据而非视图；
- `@RequestMapping`: 映射请求路径和方法，推荐使用衍生注解（`@GetMapping`/`@PostMapping`）简化写法，路径拼接需注意层级。

## web part

```html
<template>
  <div>
    <div>Bot name: {{bot_name}}</div>
    <div>Bot rating: {{bot_rating}}</div>
  </div>
  <router-view></router-view>
</template>

<script>
  import $ from "jquery";
  import { ref } from 'vue';
  
  export default {
    name: "App",
    setup: ()=>{
      let bot_name = ref("");
      let bot_rating = ref("");

      $.ajax({
        url: 'http://localhost:3000/pk/getbotinfo/',
        type: "get",
        success: resp => {
          // console.log(resp);
          bot_name.value = resp.name;
          bot_rating.value = resp.rating;
        }
      });
      
      return {
        bot_name,
        bot_rating
      }
    }
  }
</script>


<style>

  body{
    background-image: url("@/assets/background.png");
  }
</style>
```

1. 响应式核心：Vue 3 `ref()` 定义响应式变量，`setup` 内部赋值需用 `.value`，模板直接使用变量名；
2. 数据交互：通过 Ajax（jQuery/Axios）调用后端接口，需处理跨域、异常和环境变量；
3. 页面架构：`<router-view>` 实现路由嵌套，是前后端分离项目路由管理的基础；
4. 资源与样式：`@` 别名引用静态资源，`scoped` 实现样式隔离，避免全局污染；
5. 最佳实践：替换 jQuery 为 Axios，补充异常处理，使用生命周期函数 `onMounted` 发起请求，接口地址配置环境变量。