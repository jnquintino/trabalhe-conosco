import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '@/store';
import { fetchDashboardStats } from '@/store/dashboardSlice';
import Layout from '@/components/Layout/Layout';
import DashboardStats from '@/components/Dashboard/DashboardStats';
import ChartSection from '@/components/Dashboard/ChartSection';
import styled from 'styled-components';

const DashboardContainer = styled.div`
  h1 {
    color: #333;
    margin-bottom: 2rem;
    text-align: center;
  }
`;

const LoadingMessage = styled.div`
  text-align: center;
  padding: 2rem;
  color: #666;
`;

const ErrorMessage = styled.div`
  text-align: center;
  padding: 2rem;
  color: #d32f2f;
  background: #ffebee;
  border-radius: 8px;
  margin: 1rem 0;
`;

const Dashboard: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { stats, loading, error } = useSelector((state: RootState) => state.dashboard);

  useEffect(() => {
    dispatch(fetchDashboardStats());
  }, [dispatch]);

  if (loading) {
    return (
      <Layout>
        <LoadingMessage>Carregando estatísticas...</LoadingMessage>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout>
        <ErrorMessage>Erro ao carregar estatísticas: {error}</ErrorMessage>
      </Layout>
    );
  }

  if (!stats) {
    return (
      <Layout>
        <LoadingMessage>Nenhuma estatística disponível</LoadingMessage>
      </Layout>
    );
  }

  return (
    <Layout>
      <DashboardContainer>
        <h1>Dashboard - Brain Agriculture</h1>
        <DashboardStats stats={stats} />
        <ChartSection stats={stats} />
      </DashboardContainer>
    </Layout>
  );
};

export default Dashboard; 