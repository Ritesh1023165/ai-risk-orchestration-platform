class MetricsService:

    def __init__(self):
        self.total_requests = 0
        self.total_latency = 0
        self.high_risk_count = 0
        self.fraud_flag_count = 0
        self.error_count = 0

    def record_request(self, latency, result):
        self.total_requests += 1
        self.total_latency += latency

        if result.get("risk_flag") == "high":
            self.high_risk_count += 1

        if result.get("fraud_probability", 0) > 0.7:
            self.fraud_flag_count += 1
    
    def record_error(self, latency):
        self.total_requests += 1
        self.error_count +=1
        self.total_latency += latency


    def get_metrics(self):
        avg_latency = (
            self.total_latency / self.total_requests
            if self.total_requests > 0 else 0
        )

        return {
            "total_requests": self.total_requests,
            "average_latency": round(avg_latency, 4),
            "high_risk_count": self.high_risk_count,
            "fraud_flag_count": self.fraud_flag_count,
            "error_count": self.error_count
        }