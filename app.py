from flask import Flask, render_template_string
import platform
import socket
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Election & Voter Intelligence Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #0b0f19;
            color: #e2e8f0;
            font-family: 'Segoe UI', Roboto, sans-serif;
            min-height: 100vh;
        }
        .navbar-brand {
            font-weight: 800;
            font-size: 1.6rem;
            background: linear-gradient(135deg, #3b82f6, #ef4444, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card-custom {
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
            transition: all 0.25s ease-in-out;
        }
        .card-custom:hover {
            transform: translateY(-5px);
            border-color: #3b82f6;
            box-shadow: 0 12px 30px rgba(59, 130, 246, 0.2);
        }
        .status-badge {
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid #10b981;
        }
        .hero-title {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #60a5fa, #f87171, #facc15);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .progress {
            background-color: #1f2937;
            height: 12px;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg border-bottom border-secondary mb-4 py-3">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="fa-solid fa-landmark text-primary"></i> DEMOCRACY PORTAL</a>
            <span class="status-badge"><i class="fa-solid fa-shield-halved"></i> Secure Ballot Ledger Active</span>
        </div>
    </nav>

    <div class="container pb-5">
        <div class="text-center mb-5">
            <h1 class="hero-title">National Election Command Center</h1>
            <p class="text-secondary fs-5">Real-time Voter Turnout & Constituency Intelligence System</p>
        </div>

        <!-- Live Election Metrics Grid -->
        <div class="row g-4 mb-5">
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="fs-2 text-primary mb-2"><i class="fa-solid fa-boxes-stacked"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Polling Precinct Node</h5>
                    <h4 class="fw-bold text-light">{{ info.hostname }}</h4>
                    <p class="mb-0 text-muted fs-7">OS Runtime: {{ info.os }}</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="fs-2 text-success mb-2"><i class="fa-solid fa-network-wired"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Secure Cluster IP</h5>
                    <h4 class="fw-bold text-light">{{ info.ip }}</h4>
                    <p class="mb-0 text-muted fs-7">Kubernetes Pod Secure Channel</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="fs-2 text-warning mb-2"><i class="fa-solid fa-clock-rotate-left"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Sync Timestamp</h5>
                    <h4 class="fw-bold text-light">{{ info.time }} UTC</h4>
                    <p class="mb-0 text-muted fs-7">Live Auditing Active</p>
                </div>
            </div>
        </div>

        <!-- Live Voter Turnout Statistics Section -->
        <div class="card-custom p-4 mb-5">
            <h4 class="fw-bold mb-4 text-light"><i class="fa-solid fa-chart-line text-danger"></i> National Voter Turnout Analytics</h4>
            
            <label class="text-secondary mb-1">Metropolitan District Alpha (78.4% Reporting)</label>
            <div class="progress mb-3">
                <div class="progress-bar bg-primary" role="progressbar" style="width: 78.4%" aria-valuenow="78.4" aria-valuemin="0" aria-valuemax="100">78.4%</div>
            </div>

            <label class="text-secondary mb-1">Suburban Coalition Sector Beta (64.2% Reporting)</label>
            <div class="progress mb-3">
                <div class="progress-bar bg-danger" role="progressbar" style="width: 64.2%" aria-valuenow="64.2" aria-valuemin="0" aria-valuemax="100">64.2%</div>
            </div>

            <label class="text-secondary mb-1">Rural Electorate Zone Gamma (89.1% Reporting)</label>
            <div class="progress">
                <div class="progress-bar bg-success" role="progressbar" style="width: 89.1%" aria-valuenow="89.1" aria-valuemin="0" aria-valuemax="100">89.1%</div>
            </div>
        </div>

        <!-- Political Platform / Core Technology Stack -->
        <h4 class="fw-bold mb-3 text-light"><i class="fa-solid fa-scale-balanced text-warning"></i> Infrastructure Security Foundation</h4>
        <div class="row g-3">
            <div class="col-6 col-md-3">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-box-archive fa-2x text-info mb-2"></i>
                    <h6 class="mb-0">Immutable Containers</h6>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-network-wired fa-2x text-primary mb-2"></i>
                    <h6 class="mb-0">K8s Orchestration</h6>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-gears fa-2x text-danger mb-2"></i>
                    <h6 class="mb-0">Jenkins CI/CD Pipeline</h6>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-cloud-arrow-up fa-2x text-success mb-2"></i>
                    <h6 class="mb-0">AWS Cloud Infrastructure</h6>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def political_portal():
    sys_info = {
        'os': f"{platform.system()} {platform.release()}",
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'time': datetime.datetime.now().strftime("%H:%M:%S")
    }
    return render_template_string(HTML_TEMPLATE, info=sys_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
