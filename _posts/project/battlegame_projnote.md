# 创建菜单和游戏主页面
## 导航栏
### 前端

导航栏在不同功能下都有，所以可以把导航栏专门提炼出来，成专门组件，之后在不同页面复用。

习惯上，可复用组件放在component下。并且vue项目中，名称必须要有两个字母大写，例如 `NavBar.vue`

每个vue里面的组件有三个部分：
1. html：template
2. js：script
3. css：style

导航栏在style里面需要加上scoped，加上一个随机字符串，使得组件不会影响到组件以外的部分
(这里可以ai一下scoped更加详细的作用)

```html
<style scoped>

</style>
```

具体的样式可以在bootstrap中找到，实现美化的功能

在内容区域可以放一个card，这个部分可以作为一个组件，需要填充的内容在slot里面

打开某个页面，导航栏对应内容高亮

## 游戏页面（游戏地图）
### 前端
前端的过程不思考了，直接实现

# 后端与数据库的连接（主要是用户登陆相关功能的实现）
rt
使用pojo、mapping、service、controller的逻辑，实现前端的用户请求和后端相连接，并且把后端和数据库操作相关联
里面的每个模块都是一个软件包
- pojo：实现数据库中表和java类中的class的映射。`lombok`框架中的一些注解帮助我们更好映射，使得我们只需要设置class中的属性即可
  - `@Data`: 通过lombok里面的工具，自动实现一些get、tostring等基本操作
  - `@NoArgsConstructor`: 实现类的无参构造
  - `@AllArgsConstructor`: 类的有参构造
- mapping：是后端操作与数据库操作相连接的主要模块，里面的东西都是 `interface` 需要 `extends BaseMapper<>`, 其中`<>`中的内容是pojo中的数据类
  - 需要使用`@Mapper`注解
  - 在实例化的时候，需要使用`@Autowired`注解
- service: 实现业务功能，会实现多个mapping操作
  - 需要使用`@Service`注解
- controller：对接前端的请求，将其分配至对应的service上

除此之外，通过`spring-boot-starter-security`框架实现了网站的安全，需要先登陆才能继续访问其中的端口，其中需要：

实现service.impl.UserDetailsServiceImpl类，继承自UserDetailsService接口，用来接入数据库信息
实现config.SecurityConfig类，用来实现用户密码的加密存储
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

# 登陆功能的实现
基本思路：写一个接口，写一个实现，写一个controller
- Service：接口
- ServiceImpl：接口的实现
- Controller：业务逻辑实现

登陆功能包括：
- login
- register
- info
其中login和register不需要权限即可访问