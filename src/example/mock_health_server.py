
import http.server
import socketserver
import json
import random
import time
import re

PORT = 8080

class HealthScoreHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Match URL pattern: /api/v1/company/{company_id}/health-score
        match = re.search(r'/api/v1/company/([^/]+)/health-score', self.path)
        
        if match:
            company_id = match.group(1)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Generate deterministic mock data based on hash of company_id
            # This ensures the same ID always gets the same result
            seed_val = sum(ord(c) for c in company_id)
            random.seed(seed_val)
            
            overall_score = random.randint(40, 98)
            
            # Determine rating
            if overall_score >= 90: rating = "A+"
            elif overall_score >= 80: rating = "A"
            elif overall_score >= 70: rating = "B"
            elif overall_score >= 60: rating = "C"
            else: rating = "D"
            
            # Determine dimensions roughly correlated with overall score
            def get_sub_score(base):
                return min(100, max(0, base + random.randint(-10, 10)))
                
            response_data = {
                "company_id": company_id,
                "overall_score": overall_score,
                "rating": rating,
                "update_time": int(time.time()),
                "suggestion": self.get_suggestion(rating),
                "dimensions": {
                    "scale_score": get_sub_score(overall_score),
                    "innovation_score": get_sub_score(overall_score),
                    "compliance_score": get_sub_score(overall_score),
                    "stability_score": get_sub_score(overall_score)
                }
            }
            
            self.wfile.write(json.dumps(response_data, indent=2, ensure_ascii=False).encode('utf-8'))
            return
            
        # Fallback for other paths
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'{"error": "Not Found"}')

    def get_suggestion(self, rating):
        suggestions = {
            "A+": "该企业经营状况极佳，是行业标杆，建议保持当前战略。",
            "A": "企业综合实力强劲，建议关注细分领域的创新机会。",
            "B": "企业经营稳健，但在研发或合规方面有提升空间。",
            "C": "企业面临一定的经营挑战，建议进行深度风险评估。",
            "D": "企业经营风险较高，建议谨慎合作或进行合规整改。"
        }
        return suggestions.get(rating, "无建议")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), HealthScoreHandler) as or_httpd:
        print(f"Mock Business Health API serving at port {PORT}")
        print(f"Try: curl http://localhost:{PORT}/api/v1/company/company_123/health-score")
        try:
            or_httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            or_httpd.shutdown()
