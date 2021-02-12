package com.edu.data.util;


import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

//解决跨域问题
//全局配置类
@Configuration
public class WebConfig implements WebMvcConfigurer {

    /*
    * 1.访问路径
    * 2.请求来源
    * 3.方法
    * 4.允许携带
    * 5.最大时间
    * */
    //跨域对象
    @Override
    public void addCorsMappings(CorsRegistry registry){
        registry.addMapping("/**")
                .allowedOrigins("Http://localhost:8080","null") //相应地址
                .allowedMethods("GET","POST","PUT","OPTION","DELETE") //支持传输方式
                .allowCredentials(true) //是否携带信息
                .maxAge(3600);//最大相应时间
    }

}
