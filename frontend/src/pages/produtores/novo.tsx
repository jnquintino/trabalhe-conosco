import React from 'react';
import { useRouter } from 'next/router';
import { useDispatch } from 'react-redux';
import { AppDispatch } from '@/store';
import { createProdutor } from '@/store/produtoresSlice';
import Layout from '@/components/Layout/Layout';
import ProdutorForm from '@/components/Forms/ProdutorForm';
import { ProdutorCreate } from '@/types';
import toast from 'react-hot-toast';

const NovoProdutor: React.FC = () => {
  const router = useRouter();
  const dispatch = useDispatch<AppDispatch>();

  const handleSubmit = async (data: ProdutorCreate) => {
    try {
      await dispatch(createProdutor(data)).unwrap();
      toast.success('Produtor cadastrado com sucesso!');
      router.push('/produtores');
    } catch (error: any) {
      toast.error(error.message || 'Erro ao cadastrar produtor');
    }
  };

  return (
    <Layout>
      <ProdutorForm onSubmit={handleSubmit} />
    </Layout>
  );
};

export default NovoProdutor; 