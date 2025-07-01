import React from 'react';
import styled from 'styled-components';
import { DashboardStats as DashboardStatsType } from '@/types';

const StatsContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
`;

const StatCard = styled.div`
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
`;

const StatValue = styled.div`
  font-size: 2rem;
  font-weight: bold;
  color: #2e7d32;
  margin-bottom: 0.5rem;
`;

const StatLabel = styled.div`
  color: #666;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
`;

interface DashboardStatsProps {
  stats: DashboardStatsType;
}

const DashboardStats: React.FC<DashboardStatsProps> = ({ stats }) => {
  return (
    <StatsContainer>
      <StatCard>
        <StatValue>{stats.total_fazendas}</StatValue>
        <StatLabel>Total de Fazendas</StatLabel>
      </StatCard>
      <StatCard>
        <StatValue>{stats.total_hectares.toLocaleString('pt-BR')}</StatValue>
        <StatLabel>Total de Hectares</StatLabel>
      </StatCard>
      <StatCard>
        <StatValue>{Object.keys(stats.por_estado).length}</StatValue>
        <StatLabel>Estados Atendidos</StatLabel>
      </StatCard>
      <StatCard>
        <StatValue>{Object.keys(stats.por_cultura).length}</StatValue>
        <StatLabel>Tipos de Cultura</StatLabel>
      </StatCard>
    </StatsContainer>
  );
};

export default DashboardStats; 