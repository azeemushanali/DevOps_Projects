package test.sb.az.demo;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/") // Add this mapping to handle requests for "/hello"
public class hello {

    @GetMapping
    public String hello() {
        return "Hello, World! My new app";
    }

        @GetMapping("/hello")
    public String helloBaby() {
        return "baby yeah baby";
    }
}

