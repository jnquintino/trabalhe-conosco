import React, { useEffect } from 'react';
import { useRouter } from 'next/router';
import Layout from '@/components/Layout/Layout';
import ProdutorForm from '@/components/Forms/ProdutorForm';
import { ProdutorCreate, ProdutorUpdate } from '@/types';
import styled from 'styled-components';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '@/store';
import { fetchProdutor, updateProdutor } from '@/store/produtoresSlice';
import toast from 'react-hot-toast';

const Container = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.08);
`;

const EditarProdutorPage: React.FC = () => {
  const router = useRouter();
  const { id } = router.query;
  const dispatch = useDispatch<AppDispatch>();
  const { selectedProdutor: produtor, loading, error } = useSelector((state: RootState) => state.produtores);

  useEffect(() => {
    if (id && typeof id === 'string') {
      dispatch(fetchProdutor(Number(id)));
    }
  }, [dispatch, id]);

  const handleSubmit = async (data: ProdutorCreate) => {
    if (!id) return;
    try {
      await dispatch(updateProdutor({ id: Number(id), data })).unwrap();
      toast.success('Produtor atualizado com sucesso!');
      router.push(`/produtores/${id}`);
    } catch (err: any) {
      toast.error(err?.message || 'Erro ao atualizar produtor');
    }
  };

  if (loading && !produtor) {
    return (
      <Layout>
        <Container>Carregando produtor...</Container>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout>
        <Container>Erro ao carregar produtor: {error}</Container>
      </Layout>
    );
  }

  if (!produtor) {
    return (
      <Layout>
        <Container>Produtor não encontrado.</Container>
      </Layout>
    );
  }

  return (
    <Layout>
      <Container>
        <h1>Editar Produtor</h1>
        <ProdutorForm onSubmit={handleSubmit} loading={loading} defaultValues={produtor} />
      </Container>
    </Layout>
  );
};

export default EditarProdutorPage; 