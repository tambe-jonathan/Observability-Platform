package com.corporate.monitoring;

import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class BusinessMetricsConfig {

    // Tracks the number of successful transactions
    @Bean
    public Counter transactionCounter(MeterRegistry registry) {
        return Counter.builder("business_transactions_total")
                .description("Total number of completed transactions")
                .tag("status", "success")
                .register(registry);
    }
}
