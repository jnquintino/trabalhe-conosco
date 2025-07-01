import React from 'react';
import styled from 'styled-components';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';
import { DashboardStats } from '@/types';

const ChartsContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
`;

const ChartCard = styled.div`
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const ChartTitle = styled.h3`
  margin: 0 0 1rem 0;
  color: #333;
  text-align: center;
`;

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8', '#82CA9D'];

interface ChartSectionProps {
  stats: DashboardStats;
}

const ChartSection: React.FC<ChartSectionProps> = ({ stats }) => {
  const estadoData = Object.entries(stats.por_estado).map(([estado, quantidade]) => ({
    name: estado,
    value: quantidade,
  }));

  const culturaData = Object.entries(stats.por_cultura).map(([cultura, quantidade]) => ({
    name: cultura,
    value: quantidade,
  }));

  const usoSoloData = Object.entries(stats.por_uso_solo).map(([uso, area]) => ({
    name: uso,
    value: area,
  }));

  return (
    <ChartsContainer>
      <ChartCard>
        <ChartTitle>Fazendas por Estado</ChartTitle>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={estadoData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
            >
              {estadoData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </ChartCard>

      <ChartCard>
        <ChartTitle>Culturas Plantadas</ChartTitle>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={culturaData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
            >
              {culturaData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </ChartCard>

      <ChartCard>
        <ChartTitle>Uso do Solo (Hectares)</ChartTitle>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={usoSoloData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={({ name, value }) => `${name}: ${value.toLocaleString('pt-BR')} ha`}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
            >
              {usoSoloData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip formatter={(value) => `${Number(value).toLocaleString('pt-BR')} ha`} />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </ChartCard>
    </ChartsContainer>
  );
};

export default ChartSection; 