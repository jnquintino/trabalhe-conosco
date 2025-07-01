import React from 'react';
import { render, screen } from '@testing-library/react';
import DashboardStats from './DashboardStats';
import { DashboardStats as DashboardStatsType } from '@/types';

const mockStats: DashboardStatsType = {
  total_fazendas: 10,
  total_hectares: 5000.5,
  por_estado: {
    'SP': 5,
    'MG': 3,
    'GO': 2,
  },
  por_cultura: {
    'Soja': 8,
    'Milho': 5,
    'Café': 3,
  },
  por_uso_solo: {
    'Área Agricultável': 3500.0,
    'Área de Vegetação': 1500.5,
  },
};

describe('DashboardStats', () => {
  it('renders all statistics correctly', () => {
    render(<DashboardStats stats={mockStats} />);
    
    expect(screen.getByText('10')).toBeInTheDocument();
    expect(screen.getByText('5.000,5')).toBeInTheDocument();
    const elementsWith3 = screen.getAllByText('3');
    expect(elementsWith3).toHaveLength(2);
  });

  it('displays correct labels', () => {
    render(<DashboardStats stats={mockStats} />);
    
    expect(screen.getByText('Total de Fazendas')).toBeInTheDocument();
    expect(screen.getByText('Total de Hectares')).toBeInTheDocument();
    expect(screen.getByText('Estados Atendidos')).toBeInTheDocument();
    expect(screen.getByText('Tipos de Cultura')).toBeInTheDocument();
  });
}); 