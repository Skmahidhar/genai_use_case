import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { ScrollArea } from "@/components/ui/scroll-area";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";

const dataSummaries = [
  {
    title: "Fed Raises Interest Rate",
    summary: "The Federal Reserve increased interest rates by 0.25% to address inflation concerns. This may affect borrowing costs.",
    category: "Monetary Policy",
    fullText: "The full article explains the implications for corporate and consumer lending...",
    source: "Reuters"
  },
  {
    title: "China GDP Beats Forecast",
    summary: "China's economy grew by 6.3%, exceeding expectations and signaling robust recovery.",
    category: "Growth",
    fullText: "The full article discusses export trends and manufacturing rebound...",
    source: "Bloomberg"
  },
  {
    title: "Oil Prices Surge",
    summary: "Oil prices have surged past $90 a barrel amid Middle East tensions, raising concerns on energy costs.",
    category: "Commodities",
    fullText: "This report dives into OPEC reactions and global supply chain impacts...",
    source: "CNBC"
  }
];

const pieData = [
  { name: "Monetary Policy", value: 1 },
  { name: "Growth", value: 1 },
  { name: "Commodities", value: 1 }
];

const COLORS = ["#8884d8", "#82ca9d", "#ffc658"];

export default function GenAINewsDashboard() {
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  const filtered = dataSummaries.filter((item) =>
    item.title.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar Logo */}
      <div className="w-48 bg-white shadow-md flex flex-col items-center justify-center">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg"
          alt="Logo"
          className="w-20 h-20"
        />
        <h1 className="text-lg font-bold mt-2">GenAI News</h1>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-6 space-y-6">
        <div className="flex justify-between items-center">
          <h2 className="text-2xl font-semibold">Daily Summaries</h2>
          <Input
            placeholder="Search News..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-1/3"
          />
        </div>

        {/* Summary Slider */}
        <ScrollArea className="whitespace-nowrap overflow-x-auto flex space-x-4">
          {filtered.map((item, index) => (
            <motion.div
              key={index}
              whileHover={{ scale: 1.05 }}
              className="inline-block min-w-[300px]"
            >
              <Card
                className="cursor-pointer hover:shadow-lg"
                onClick={() => navigate(`/news/${index}`)}
              >
                <CardContent className="p-4">
                  <h3 className="text-lg font-bold">{item.title}</h3>
                  <p className="text-sm text-gray-600 mt-2">{item.summary}</p>
                  <span className="text-xs text-blue-600 mt-1 block">
                    {item.source}
                  </span>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </ScrollArea>

        {/* Charts */}
        <div className="grid grid-cols-2 gap-6">
          <div className="bg-white rounded-2xl p-4 shadow">
            <h3 className="text-lg font-medium mb-2">Category Breakdown</h3>
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie
                  dataKey="value"
                  isAnimationActive={false}
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  outerRadius={80}
                  label
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
              </PieChart>
            </ResponsiveContainer>
          </div>

          <div className="bg-white rounded-2xl p-4 shadow">
            <h3 className="text-lg font-medium mb-2">Article Count by Source</h3>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={dataSummaries}>
                <XAxis dataKey="source" />
                <YAxis />
                <Tooltip />
                <Bar dataKey={() => 1} fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
