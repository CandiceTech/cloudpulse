import { useEffect, useState } from "react";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

function App() {

  const [instances, setInstances] = useState([]);
  const [summary, setSummary] = useState(null);
  const [buckets, setBuckets] = useState([]);

  useEffect(() => {

    fetch("http://localhost:8000/ec2/idle")
      .then((res) => res.json())
      .then((data) => setInstances(data));

    fetch("http://localhost:8000/analytics/summary")
      .then((res) => res.json())
      .then((data) => setSummary(data));

    fetch("http://localhost:8000/s3/analyze")
      .then((res) => res.json())
      .then((data) => setBuckets(data));

  }, []);

  const riskData = [
    {
      name: "HIGH",
      value: instances.filter(
        (i) => i.risk_level === "HIGH"
      ).length
    },
    {
      name: "MEDIUM",
      value: instances.filter(
        (i) => i.risk_level === "MEDIUM"
      ).length
    },
    {
      name: "LOW",
      value: instances.filter(
        (i) => i.risk_level === "LOW"
      ).length
    }
  ];

  const cpuData = instances.map((instance) => ({
    name: instance.instance_id.slice(-5),
    cpu: instance.avg_cpu
  }));

  return (

    <div style={styles.page}>

      {/* Sidebar */}
      <div style={styles.sidebar}>

        <h1 style={styles.logo}>
          CloudPulse
        </h1>

        <div style={styles.navItem}>
          Dashboard
        </div>

        <div style={styles.navItem}>
          EC2 Optimization
        </div>

        <div style={styles.navItem}>
          S3 Optimization
        </div>

        <div style={styles.navItem}>
          Analytics
        </div>

      </div>

      {/* Main */}
      <div style={styles.main}>

        <h1 style={styles.title}>
          AWS Cloud Optimization Dashboard
        </h1>

        <p style={styles.subtitle}>
          Monitor infrastructure waste and optimization opportunities.
        </p>

        {/* Cards */}
        <div style={styles.cardGrid}>

          <div style={styles.card}>

            <h3>Instances Analyzed</h3>

            <h2 style={styles.metric}>
              {summary?.instances_analyzed || 0}
            </h2>

          </div>

          <div style={styles.card}>

            <h3>Monthly Savings</h3>

            <h2
              style={{
                ...styles.metric,
                color: "green"
              }}
            >
              $
              {summary?.total_monthly_savings || 0}
            </h2>

          </div>

          <div style={styles.card}>

            <h3>Annual Savings</h3>

            <h2
              style={{
                ...styles.metric,
                color: "#2563eb"
              }}
            >
              $
              {summary?.total_annual_savings || 0}
            </h2>

          </div>

        </div>

        {/* Charts */}
        <div style={styles.chartGrid}>

          {/* Risk */}
          <div style={styles.chartCard}>

            <h2>
              Risk Distribution
            </h2>

            <ResponsiveContainer
              width="100%"
              height={300}
            >

              <PieChart>

                <Pie
                  data={riskData}
                  dataKey="value"
                  outerRadius={100}
                  label
                >

                  <Cell fill="#ef4444" />
                  <Cell fill="#f59e0b" />
                  <Cell fill="#22c55e" />

                </Pie>

                <Tooltip />

              </PieChart>

            </ResponsiveContainer>

          </div>

          {/* CPU */}
          <div style={styles.chartCard}>

            <h2>
              CPU Utilization
            </h2>

            <ResponsiveContainer
              width="100%"
              height={300}
            >

              <BarChart data={cpuData}>

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="name" />

                <YAxis />

                <Tooltip />

                <Bar
                  dataKey="cpu"
                  fill="#3b82f6"
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>

        {/* EC2 Table */}
        <div style={styles.tableCard}>

          <h2>
            EC2 Optimization Recommendations
          </h2>

          <table style={styles.table}>

            <thead>

              <tr>

                <th style={styles.th}>
                  Instance
                </th>

                <th style={styles.th}>
                  CPU
                </th>

                <th style={styles.th}>
                  Risk
                </th>

                <th style={styles.th}>
                  Savings
                </th>

                <th style={styles.th}>
                  Recommendation
                </th>

              </tr>

            </thead>

            <tbody>

              {instances.map((instance) => (

                <tr key={instance.instance_id}>

                  <td style={styles.td}>
                    {instance.instance_id}
                  </td>

                  <td style={styles.td}>
                    {instance.avg_cpu}%
                  </td>

                  <td style={styles.td}>

                    <span
                      style={{
                        color:
                          instance.risk_level === "HIGH"
                            ? "red"
                            : "orange",
                        fontWeight: "bold"
                      }}
                    >
                      {instance.risk_level}
                    </span>

                  </td>

                  <td style={styles.td}>
                    $
                    {instance.potential_monthly_savings}
                  </td>

                  <td style={styles.td}>
                    {instance.recommendation}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

        {/* S3 Table */}
        <div style={styles.tableCard}>

          <h2>
            S3 Storage Optimization
          </h2>

          <table style={styles.table}>

            <thead>

              <tr>

                <th style={styles.th}>
                  Bucket
                </th>

                <th style={styles.th}>
                  Storage
                </th>

                <th style={styles.th}>
                  Monthly Cost
                </th>

                <th style={styles.th}>
                  Recommendation
                </th>

              </tr>

            </thead>

            <tbody>

              {buckets.map((bucket) => (

                <tr key={bucket.bucket_name}>

                  <td style={styles.td}>
                    {bucket.bucket_name}
                  </td>

                  <td style={styles.td}>
                    {bucket.estimated_storage_gb} GB
                  </td>

                  <td style={styles.td}>
                    $
                    {bucket.estimated_monthly_cost}
                  </td>

                  <td style={styles.td}>
                    {bucket.recommendation}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>

  );
}

const styles = {

  page: {
    display: "flex",
    backgroundColor: "#f1f5f9",
    minHeight: "100vh",
    fontFamily: "Arial"
  },

  sidebar: {
    width: "250px",
    backgroundColor: "#0f172a",
    color: "white",
    padding: "30px"
  },

  logo: {
    marginBottom: "40px",
    fontSize: "32px"
  },

  navItem: {
    padding: "15px",
    marginBottom: "10px",
    backgroundColor: "#1e293b",
    borderRadius: "10px",
    cursor: "pointer"
  },

  main: {
    flex: 1,
    padding: "40px"
  },

  title: {
    fontSize: "36px",
    marginBottom: "10px"
  },

  subtitle: {
    color: "#64748b",
    marginBottom: "40px"
  },

  cardGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "20px",
    marginBottom: "40px"
  },

  card: {
    backgroundColor: "white",
    padding: "25px",
    borderRadius: "15px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  },

  metric: {
    fontSize: "36px",
    marginTop: "10px"
  },

  chartGrid: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "20px",
    marginBottom: "40px"
  },

  chartCard: {
    backgroundColor: "white",
    padding: "20px",
    borderRadius: "15px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  },

  tableCard: {
    backgroundColor: "white",
    padding: "20px",
    borderRadius: "15px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    marginBottom: "40px",
    overflowX: "auto"
  },

  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "20px"
  },

  th: {
    textAlign: "left",
    padding: "14px",
    borderBottom: "2px solid #e2e8f0",
    color: "#334155"
  },

  td: {
    padding: "14px",
    borderBottom: "1px solid #e2e8f0",
    fontSize: "14px"
  }

};

export default App;